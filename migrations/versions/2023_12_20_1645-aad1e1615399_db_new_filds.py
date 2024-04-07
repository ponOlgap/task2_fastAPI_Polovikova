"""DB_new_filds

Revision ID: aad1e1615399
Revises: 1c035a00f775
Create Date: 2023-1al2-20 16:45:45.133513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aad1e1615399'
down_revision: Union[str, None] = '1c035a00f775'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categor', sa.Column('num', sa.String(), nullable=True))
    op.create_index(op.f('ix_categor_num'), 'categor', ['num'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_categor_num'), table_name='categor')
    op.drop_column('categor', 'num')
    # ### end Alembic commands ###
