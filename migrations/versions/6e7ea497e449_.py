"""empty message

Revision ID: 6e7ea497e449
Revises: 9225d44e394f
Create Date: 2020-05-03 17:33:25.168116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e7ea497e449'
down_revision = '9225d44e394f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('numTelefono', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'numTelefono')
    # ### end Alembic commands ###