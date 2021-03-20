"""empty message

Revision ID: e5d8b877896d
Revises: 
Create Date: 2020-05-02 13:51:18.751366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5d8b877896d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evento',
    sa.Column('idEvento', sa.Integer(), nullable=False),
    sa.Column('Nombre', sa.String(length=100), nullable=False),
    sa.Column('Siglas', sa.String(length=30), nullable=False),
    sa.Column('Decripcion', sa.String(length=500), nullable=False),
    sa.Column('Duracion', sa.String(length=50), nullable=False),
    sa.Column('Cupo', sa.Integer(), nullable=False),
    sa.Column('Costo', sa.Integer(), nullable=False),
    sa.Column('Lugar', sa.String(length=100), nullable=False),
    sa.Column('Fecha', sa.DateTime(), nullable=False),
    sa.Column('imagen', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('idEvento')
    )
    op.create_table('boleto',
    sa.Column('folio', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('idEvento', sa.Integer(), nullable=True),
    sa.Column('Fecha', sa.DateTime(), nullable=False),
    sa.Column('Asiento', sa.Integer(), nullable=False),
    sa.Column('imagen', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['idEvento'], ['evento.idEvento'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('folio')
    )
    op.add_column('user', sa.Column('edad', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('empresa', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('nombreCompleto', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('numTelefono', sa.String(length=20), nullable=False))
    op.add_column('user', sa.Column('residencia', sa.String(length=70), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'residencia')
    op.drop_column('user', 'numTelefono')
    op.drop_column('user', 'nombreCompleto')
    op.drop_column('user', 'empresa')
    op.drop_column('user', 'edad')
    op.drop_table('boleto')
    op.drop_table('evento')
    # ### end Alembic commands ###