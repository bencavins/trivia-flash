"""add cards table

Revision ID: 67efb95b131a
Revises: 
Create Date: 2024-03-27 13:20:55.372090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67efb95b131a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cards'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    # ### end Alembic commands ###