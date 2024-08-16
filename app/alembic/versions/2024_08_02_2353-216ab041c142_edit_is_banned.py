"""edit is banned

Revision ID: 216ab041c142
Revises: 83468e1f4380
Create Date: 2024-08-02 23:53:41.994584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '216ab041c142'
down_revision: Union[str, None] = '83468e1f4380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proxys', sa.Column('is_banned', sa.Boolean(), nullable=True))
    op.drop_column('proxys', '_is_banned')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proxys', sa.Column('_is_banned', sa.BOOLEAN(), nullable=True))
    op.drop_column('proxys', 'is_banned')
    # ### end Alembic commands ###
