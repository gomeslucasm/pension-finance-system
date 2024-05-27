"""craete plano operation tables

Revision ID: 211e5ad188b7
Revises: ef084a145087
Create Date: 2024-05-27 02:30:53.124011

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '211e5ad188b7'
down_revision: Union[str, None] = 'ef084a145087'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plano_operations',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('id_plano', sa.UUID(), nullable=False),
    sa.Column('operation_type', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_plano'], ['planos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plano_operations')
    # ### end Alembic commands ###