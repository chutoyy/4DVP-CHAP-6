"""empty message

Revision ID: 424808e1fe49
Revises: d4392342465f
Create Date: 2021-08-20 12:11:57.901994

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from psycopg2 import errors
from psycopg2.errorcodes import DUPLICATE_OBJECT

# revision identifiers, used by Alembic.
revision = '424808e1fe49'
down_revision = 'd4392342465f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.execute('CREATE EXTENSION pg_trgm')
    # thanks to https://stackoverflow.com/a/58743364/1428034 !
    except sa.exc.ProgrammingError as e:
        if isinstance(e.orig, errors.lookup(DUPLICATE_OBJECT)):
            print(">>> pg_trgm already loaded, ignore")
            op.execute("Rollback")

    op.create_index('note_pg_trgm_index', 'alias', ['note'], unique=False, postgresql_ops={'note': 'gin_trgm_ops'}, postgresql_using='gin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('note_pg_trgm_index', table_name='alias')
    op.execute('DROP EXTENSION pg_trgm')
    # ### end Alembic commands ###
