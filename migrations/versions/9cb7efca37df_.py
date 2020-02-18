"""empty message

Revision ID: 9cb7efca37df
Revises: 1063f6780afd
Create Date: 2019-11-29 20:11:59.172217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb7efca37df'
down_revision = '1063f6780afd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('name', sa.String(length=80), nullable=True))
    op.drop_column('usuario', 'last_name')
    op.drop_column('usuario', 'first_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('usuario', sa.Column('last_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('usuario', 'name')
    # ### end Alembic commands ###