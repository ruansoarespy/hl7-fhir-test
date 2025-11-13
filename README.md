# HL7 FHIR Test

Projeto para configuração de um **servidor FHIR local** utilizando **HAPI FHIR** e **PostgreSQL** via Docker Compose, com pipeline de carga de dados para o Resource `Patient` e `Observation`.

## Estrutura do projeto

- `docker-compose.yml` — Arquivo para subir o servidor HAPI FHIR e o PostgreSQL via Docker.
- `data/` — Pasta com arquivos CSV de teste (`patients.csv`).
- `src/` — Scripts Python para carga de dados (`load_patients.py`).
- `docs/` — Documentação com passo a passo de configuração, execução e testes.
- `README.md` — Visão geral do projeto.

## Sobre

Este projeto tem como objetivo:

1. Configurar um servidor FHIR local (HAPI FHIR) com persistência em PostgreSQL.
2. Permitir carga de dados de pacientes e observações usando **PySpark**.
3. Testar endpoints FHIR como `/Patient` e `/Observation`.
4. Documentar todo o processo para fácil reprodução.

## Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.10+
- Virtualenv ou ambiente de preferência para Python
- PySpark e Requests instalados (`pip install pyspark requests`)

## Como usar

1. Clonar o repositório:
   git clone https://github.com/ruansoarespy/hl7-fhir-test.git
   cd hl7-fhir-test

2. Subir o servidor FHIR e PostgreSQL:
   docker-compose up -d

3. Criar e ativar o ambiente virtual Python:
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt

4. Rodar o script de carga de dados:
   python src/load_patients.py

5. Verificar dados no servidor FHIR:
   - Acesse http://localhost:8080/fhir/Patient para listar pacientes.
   - Acesse http://localhost:8080/fhir/Observation para listar observações.

## Documentação

- Todos os passos de instalação, configuração e execução estão detalhados em `docs/`.
- Inclui instruções para testes, criação de recursos e visualização no HAPI FHIR.

## Contato

- Ruan Ferreira Soares
- GitHub: [ruansoarespy](https://github.com/ruansoarespy)

