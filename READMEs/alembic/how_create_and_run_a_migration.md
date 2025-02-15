# TLDR

Documenting the steps of creating and running a migration for future reference

## Steps

- alembic revision -m "add reset token to account table"
- then fill in the upgrade & downgrade logic
- alembic upgrade head

## Tips

- If you run into issues, try some of these commands...
    - alembic downgrade -1
    - alembic history
    - alembic current