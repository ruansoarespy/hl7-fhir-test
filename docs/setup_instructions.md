Parte 1 — Configuração do Servidor FHIR

Objetivo:
Subir um servidor FHIR local (HAPI FHIR) com persistência em PostgreSQL.

Arquitetura e Ferramentas:
- Servidor FHIR: HAPI FHIR (R4)
- Banco de dados: PostgreSQL 14
- Orquestração: Docker + Docker Compose

Estrutura de pastas:
hl7-fhir-test/
├─ data/         # (opcional) arquivos persistentes
├─ docs/         # documentação
└─ docker-compose.yml

Passos de instalação e configuração:

1. Instalar Docker e Docker Compose.

2. Criar pastas do projeto:
   mkdir hl7-fhir-test
   cd hl7-fhir-test
   mkdir data docs

3. Criar o arquivo docker-compose.yml (conteúdo acima).

4. Subir os containers:
   docker compose up -d
   docker ps

   - Devem aparecer 2 containers: fhir_postgres e hapi_fhir_server.
   - Aguarde alguns segundos até o healthcheck do HAPI FHIR ficar "healthy".

5. Testar servidor:
   curl http://localhost:8080/fhir/metadata | head -n 20

6. Criar recurso de teste (Patient):

   Criar arquivo patient.json:
   {
     "resourceType": "Patient",
     "name": [{"family": "Soares", "given": ["Ruan"]}],
     "gender": "male",
     "birthDate": "2004-09-22"
   }

   Enviar recurso:
   curl -X POST -H "Content-Type: application/fhir+json" -d @patient.json http://localhost:8080/fhir/Patient

7. Listar pacientes cadastrados:
   curl http://localhost:8080/fhir/Patient?_count=5

Resultado final:
- Servidor HAPI FHIR rodando localmente (porta 8080).
- Banco PostgreSQL ativo e persistente.
- Capaz de receber e consultar recursos FHIR (Patient).
- Documentação e Docker Compose prontos para entrega.
