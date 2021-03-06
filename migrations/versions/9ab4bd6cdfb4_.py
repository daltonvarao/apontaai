"""empty message

Revision ID: 9ab4bd6cdfb4
Revises: f3de023010d5
Create Date: 2019-11-28 16:09:07.925305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ab4bd6cdfb4'
down_revision = 'f3de023010d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('first_name', sa.String(length=100), nullable=True))
    op.drop_column('usuario', 'firs_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('firs_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('usuario', 'first_name')
    # ### end Alembic commands ###
