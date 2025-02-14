# kmeleon-agent-api

Info regard Tad Duval's technical assessment

## Initial setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install uv
uv init
uv run hello.py
rm hello.py
```

## Scaffold project

```sh
mkdir src
mkdir src/db
mkdir src/routers
mkdir src/routers/healthcheck
touch src/routers/healthcheck/router.py
touch src/main.py
mkdir test
```

## Next steps

- add code to main.py
- add code to src/routers/healthcheck/router.py
- install packages
```sh
uv add fastapi python-dotenv slowapi debugpy uvicorn
```

## Run for the 1st time

- `uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload`
```sh
curl localhost:8000
```