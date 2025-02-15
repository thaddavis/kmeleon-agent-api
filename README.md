# kmeleon-agent-api

Info regarding Tad Duval's technical assessment

## Initial setup

```sh
python -m venv .venv
source .venv/bin/activate
uv sync
```

## How to run the API

- `uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload`

## Running a local PostgresDB application

- `https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/#with-a-connection-pool`
- `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`

## Useful links

- https://langchain-ai.github.io/langgraph/
- https://python.langchain.com/docs/introduction/
- https://openweathermap.org/api/one-call-3