"""

Revision ID: 337eb693eddf
Revises: f84c3da2c9ee
Create Date: 2024-11-06 14:07:47.096542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '337eb693eddf'
down_revision: Union[str, None] = 'f84c3da2c9ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('original_creation_equipment_rewards', sa.Column('original_creation_id', sa.Integer(), nullable=False))
    op.drop_index('ix_original_creation_equipment_rewards_original_creations_id', table_name='original_creation_equipment_rewards')
    op.create_index(op.f('ix_original_creation_equipment_rewards_original_creation_id'), 'original_creation_equipment_rewards', ['original_creation_id'], unique=False)
    op.drop_constraint('original_creation_equipment_rewards_original_creations_id_fkey', 'original_creation_equipment_rewards', type_='foreignkey')
    op.create_foreign_key(None, 'original_creation_equipment_rewards', 'original_creations', ['original_creation_id'], ['id'], onupdate='CASCADE')
    op.drop_column('original_creation_equipment_rewards', 'original_creations_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('original_creation_equipment_rewards', sa.Column('original_creations_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'original_creation_equipment_rewards', type_='foreignkey')
    op.create_foreign_key('original_creation_equipment_rewards_original_creations_id_fkey', 'original_creation_equipment_rewards', 'original_creations', ['original_creations_id'], ['id'], onupdate='CASCADE')
    op.drop_index(op.f('ix_original_creation_equipment_rewards_original_creation_id'), table_name='original_creation_equipment_rewards')
    op.create_index('ix_original_creation_equipment_rewards_original_creations_id', 'original_creation_equipment_rewards', ['original_creations_id'], unique=False)
    op.drop_column('original_creation_equipment_rewards', 'original_creation_id')
    # ### end Alembic commands ###