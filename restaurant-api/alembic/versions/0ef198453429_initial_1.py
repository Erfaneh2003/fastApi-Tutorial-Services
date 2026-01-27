"""initial-1

Revision ID: 0ef198453429
Revises: 44826bf7a579
Create Date: 2026-01-24 16:11:52.634558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ef198453429'
down_revision: Union[str, Sequence[str], None] = '44826bf7a579'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
