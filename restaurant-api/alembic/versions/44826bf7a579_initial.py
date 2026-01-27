"""initial

Revision ID: 44826bf7a579
Revises: e418c7aea552
Create Date: 2026-01-24 15:18:54.986941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44826bf7a579'
down_revision: Union[str, Sequence[str], None] = 'e418c7aea552'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
