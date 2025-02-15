"""add accounts table

Revision ID: e60100701396
Revises: e04a7770dbe9
Create Date: 2025-02-15 01:36:03.771590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e60100701396'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    """Apply the migration: Create accounts table."""
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('email', sa.String(), unique=True, index=True, nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('reset_token', sa.String(), nullable=True),
    )

def downgrade():
    """Rollback the migration: Drop accounts table."""
    op.drop_table('accounts')
