"""empty message

Revision ID: 0176a13f9778
Revises: 9b203713254a
Create Date: 2024-08-25 01:25:56.937448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0176a13f9778'
down_revision: Union[str, None] = '9b203713254a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'subscribe', ['tg_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscribe', type_='unique')
    # ### end Alembic commands ###
