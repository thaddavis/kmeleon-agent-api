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
