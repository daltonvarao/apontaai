"""empty message

Revision ID: 4552b1fc5055
Revises: 286fc868b6bf
Create Date: 2019-11-27 23:39:43.755116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4552b1fc5055'
down_revision = '286fc868b6bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('first_name', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'first_name')
    # ### end Alembic commands ###
