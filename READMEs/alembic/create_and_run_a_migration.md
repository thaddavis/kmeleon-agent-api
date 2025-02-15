# TLDR

Documenting the steps of creating and running a migration for future reference

## log

- alembic revision -m "add reset token to account table"
- fill in the upgrade & downgrade logic
- alembic upgrade head

## TIP

- If you run into issues, try some of these commands...
    - alembic downgrade -1
    - alembic history
    - alembic current