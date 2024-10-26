"""Aggiunta

Revision ID: 67d288c984e4
Revises: be361e5e4354
Create Date: 2024-10-23 19:27:47.816839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67d288c984e4'
down_revision: Union[str, None] = 'be361e5e4354'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_area_conquests_created'), 'area_conquests', ['created'], unique=False)
    op.drop_constraint('area_conquests_zone_id_fkey', 'area_conquests', type_='foreignkey')
    op.create_foreign_key(None, 'area_conquests', 'zones', ['zone_id'], ['id'])
    op.drop_constraint('fiends_zone_id_fkey', 'fiends', type_='foreignkey')
    op.drop_constraint('fiends_species_conquest_id_fkey', 'fiends', type_='foreignkey')
    op.create_foreign_key(None, 'fiends', 'species_conquests', ['species_conquest_id'], ['id'])
    op.create_foreign_key(None, 'fiends', 'zones', ['zone_id'], ['id'])
    op.create_index(op.f('ix_original_creations_created'), 'original_creations', ['created'], unique=False)
    op.create_index(op.f('ix_species_conquests_created'), 'species_conquests', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_species_conquests_created'), table_name='species_conquests')
    op.drop_index(op.f('ix_original_creations_created'), table_name='original_creations')
    op.drop_constraint(None, 'fiends', type_='foreignkey')
    op.drop_constraint(None, 'fiends', type_='foreignkey')
    op.create_foreign_key('fiends_species_conquest_id_fkey', 'fiends', 'species_conquests', ['species_conquest_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('fiends_zone_id_fkey', 'fiends', 'zones', ['zone_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint(None, 'area_conquests', type_='foreignkey')
    op.create_foreign_key('area_conquests_zone_id_fkey', 'area_conquests', 'zones', ['zone_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_index(op.f('ix_area_conquests_created'), table_name='area_conquests')
    # ### end Alembic commands ###
