"""tag

Revision ID: 4938628efe1c
Revises: 8a91510fa45d
Create Date: 2020-01-13 20:28:48.854494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4938628efe1c'
down_revision = '8a91510fa45d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###