# TLDR

Tad Duval's technical assessment. The challenge was to build a ReAct agent with a few tools for connecting to the
OpenWeather API using the FastAPI framework. This solution includes setup for running the application in Docker, Authentication,
Monitoring with LangSmith & Rate Limiting.

## How to run the API with Docker Compose (RECOMMENDED)

1. copy the `.env.tmplt` to a `.env` file at the root of the project
1. add the following environment variables to the .env
  - `OPENAI_API_KEY` (https://platform.openai.com/)
  - `OPENWEATHER_API_KEY` (http://openweathermap.org/)
  - `LANGSMITH_API_KEY` (https://www.langchain.com/langsmith)
1. Make sure the.env file has the following variable
  - `POSTGRES_URL=postgresql://postgres:mysecretpassword@db:5432/postgres?sslmode=disable`
    - NOTE: `db` is the appropriate db hostname when running in docker 🔑
1. `docker-compose up`

## How to run the API in steps on your machine

1. `python -m venv .venv`
1. `source .venv/bin/activate`
1. `uv sync`
1. copy the `.env.tmplt` to a `.env` file at the root of the project
1. add the following environment variables to the .env
  - `OPENAI_API_KEY` (https://platform.openai.com/)
  - `OPENWEATHER_API_KEY` (http://openweathermap.org/)
  - `LANGSMITH_API_KEY` (https://www.langchain.com/langsmith)
1. make sure the.env file has the following variable
  - `POSTGRES_URL=postgresql://postgres:mysecretpassword@localhost:5432/postgres?sslmode=disable`
    - NOTE: `localhost` is the appropriate db hostname when running on your machine 🔑
1. `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`
1. RUN MIGRATIONS! `uv run alembic upgrade head`
1. `uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload`

## Useful links

- https://langchain-ai.github.io/langgraph/
- https://python.langchain.com/docs/introduction/
- https://openweathermap.org/api/one-call-3

## How to test the API

Import the `test/kmeleon-agent-api.postman_collection.json` file into POSTMAN

Suggested order to test with POSTMAN would be...

1. `create account`
1. `log in`
1. `chat`

## Test curl command for  just in case

"content" - represents the prompt
"thread_id" - is the conversation thread

```sh
curl -X POST "http://localhost:8000/api/chat" \
     -H "Content-Type: application/json" \
     -d '{"content": "Hello, my name is Tad!","thread_id": "1"}'
```  