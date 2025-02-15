## Setting up Alembic

```sh
uv add alembic
uv run alembic init alembic
```

Then tweaked the `alembic/env.py` file to pull the POSTGRES_URL from the .env file

## FYI

```sh
uv run alembic upgrade head
uv run alembic history
```

## FYI undo the first migration

```sh
uv run alembic downgrade base
uv run alembic current
uv run alembic history
```

## Doing the migration after sorting out the 

```sh
uv run alembic revision --autogenerate -m "Sync database schema"
```