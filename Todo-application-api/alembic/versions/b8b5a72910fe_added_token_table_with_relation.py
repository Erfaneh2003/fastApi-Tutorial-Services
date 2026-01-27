from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'b8b5a72910fe'
down_revision: Union[str, Sequence[str], None] = '2991fa8c94ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ایجاد جدول token (بدون فاصله!)
    op.create_table(
        'token',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column(
            'created_date',
            sa.DateTime(),
            server_default=sa.text('CURRENT_TIMESTAMP'),
            nullable=True
        ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('token', name='uq_token_token')
    )

    # تغییر ستون username با batch (ویژه SQLite)
    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column(
            'username',
            existing_type=sa.String(length=250),
            type_=sa.String(length=72),
            existing_nullable=False
        )
        batch_op.create_unique_constraint(
            'uq_users_username',
            ['username']
        )


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint(
            'uq_users_username',
            type_='unique'
        )
        batch_op.alter_column(
            'username',
            existing_type=sa.String(length=72),
            type_=sa.String(length=250),
            existing_nullable=False
        )

    op.drop_table('token')
