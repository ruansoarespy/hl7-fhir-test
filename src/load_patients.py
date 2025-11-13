from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split
import requests
import json

# URL do servidor FHIR local
FHIR_URL = "http://localhost:8080/fhir"

# Criação da Spark Session
spark = SparkSession.builder \
    .appName("PatientETL") \
    .getOrCreate()

# Leitura do CSV (caminho corrigido e encoding UTF-8)
df = spark.read.csv("data/patients.csv", header=True, sep=",", encoding="UTF-8")

# Criar coluna de Observações como array
df = df.withColumn("ObservacoesArray", split(col("Observação"), "\|"))

# Função para criar recurso Patient
def create_patient_resource(row):
    return {
        "resourceType": "Patient",
        "name": [
            {"text": row["Nome"]}
        ],
        "gender": "male" if row["Gênero"].lower().startswith("m") else "female",
        "birthDate": "-".join(reversed(row["Data de Nascimento"].split("/"))),
        "telecom": [
            {"system": "phone", "value": row["Telefone"]}
        ],
        "identifier": [
            {
                "system": "https://gov.br/cpf",
                "value": row["CPF"]
            }
        ],
        "extension": [
            {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
                "valueAddress": {
                    "country": row["País de Nascimento"]
                }
            }
        ]
    }

# Função para criar recurso Observation
def create_observation_resource(code_text, patient_id):
    return {
        "resourceType": "Observation",
        "status": "final",
        "code": {
            "text": code_text
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        }
    }

# Função para enviar recurso ao FHIR
def send_to_fhir(resource):
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(f"{FHIR_URL}/{resource['resourceType']}", 
                             data=json.dumps(resource), 
                             headers=headers)
    try:
        return response.json()
    except:
        return {"error": "invalid json response", "raw": response.text}

# Coletar todas as linhas do DataFrame
rows = df.collect()

# Loop para enviar pacientes e observações
for row in rows:
    patient_json = create_patient_resource(row.asDict())
    response = send_to_fhir(patient_json)

    if "id" not in response:
        print("Erro criando paciente:", response)
        continue

    patient_id = response["id"]

    if row["Observação"] and row["Observação"].strip() != "":
        for obs_text in row["ObservacoesArray"]:
            observation_json = create_observation_resource(obs_text, patient_id)
            obs_response = send_to_fhir(observation_json)
            print("Observation criada:", obs_response)

# Encerrar Spark
spark.stop()
