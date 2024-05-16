"""Ajout du don.

Revision ID: e00a1367bde0
Revises: 77d5e01f0469
Create Date: 2024-05-15 16:32:53.323584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e00a1367bde0'
down_revision = '77d5e01f0469'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('montant', sa.Float(), nullable=False),
    sa.Column('identifiant', sa.String(length=255), nullable=False),
    sa.Column('telephone', sa.String(length=10), nullable=False),
    sa.Column('modePayement', sa.String(length=10), nullable=False),
    sa.Column('projet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['projet_id'], ['projet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dons')
    # ### end Alembic commands ###
