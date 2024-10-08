"""empty message

Revision ID: e40bd5c55e8e
Revises: 0176a13f9778
Create Date: 2024-08-31 15:13:03.880927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e40bd5c55e8e'
down_revision: Union[str, None] = '0176a13f9778'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_register', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_register')
    # ### end Alembic commands ###
