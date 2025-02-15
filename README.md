# kmeleon-agent-api

Info regarding Tad Duval's technical assessment

## Initial setup

```sh
python -m venv .venv
source .venv/bin/activate
uv sync
```

## How to run the API with Docker Compose (RECOMMENDED)

- copy the `.env.tmplt` to a `.env` file at the root of the project
- add the following environment variables to the .env
  - `OPENAI_API_KEY` (https://platform.openai.com/)
  - `OPENWEATHER_API_KEY` (http://openweathermap.org/)
  - `LANGSMITH_API_KEY` (https://www.langchain.com/langsmith)
- `docker-compose up`

## How to run the API in steps

- `uv sync`
- copy the `.env.tmplt` to a `.env` file at the root of the project
- add the following environment variables to the .env
  - `OPENAI_API_KEY` (https://platform.openai.com/)
  - `OPENWEATHER_API_KEY` (http://openweathermap.org/)
  - `LANGSMITH_API_KEY` (https://www.langchain.com/langsmith)
- `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`
- `uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload`

## Useful links

- https://langchain-ai.github.io/langgraph/
- https://python.langchain.com/docs/introduction/
- https://openweathermap.org/api/one-call-3

## How to test the API

Import the `kmeleon-agent-api.postman_collection.json` file into POSTMAN