"""Add registration_info column

Revision ID: 6d925e9b5ab2
Revises: 
Create Date: 2023-11-23 01:03:21.715821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d925e9b5ab2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('participant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registration_info', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('participant', schema=None) as batch_op:
        batch_op.drop_column('registration_info')

    # ### end Alembic commands ###