"""empty message

Revision ID: be5969f7b86b
Revises: 04b7bb38cff2
Create Date: 2019-11-28 16:16:52.041148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be5969f7b86b'
down_revision = '04b7bb38cff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'adv')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('adv', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
