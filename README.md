# HL7 FHIR Test

Projeto para configuração de um **servidor FHIR local** utilizando **HAPI FHIR** e **PostgreSQL** via Docker Compose.

## Estrutura do projeto

- `docker-compose.yml` — Arquivo para subir o servidor HAPI FHIR e o PostgreSQL via Docker.
- `data/` — Pasta para armazenar arquivos de dados de teste.
- `docs/` — Documentação com passo a passo de configuração e testes.
- `README.md` — Visão geral do projeto.

## Sobre

O objetivo deste projeto é:

1. Configurar um servidor FHIR local, sem uso de soluções cloud.
2. Criar persistência de dados usando PostgreSQL.
3. Permitir testes de endpoints FHIR, como `/Patient` e `/Observation`.
4. Documentar todo o processo para reprodução.

## Como usar

1. Clonar o repositório:
   ```bash
   git clone https://github.com/ruansoarespy/hl7-fhir-test.git
   cd hl7-fhir-test
