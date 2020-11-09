"""empty message

Revision ID: 500fe366de15
Revises: 3438f4721384
Create Date: 2020-11-07 16:40:50.050217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500fe366de15'
down_revision = '3438f4721384'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cn', sa.Column('client', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cn', 'client')
    # ### end Alembic commands ###