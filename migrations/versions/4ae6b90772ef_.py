"""empty message

Revision ID: 4ae6b90772ef
Revises: e787b4b2b24e
Create Date: 2025-01-07 16:01:23.422399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ae6b90772ef'
down_revision = 'e787b4b2b24e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=108),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('image_filename',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=150),
               existing_nullable=True)
        batch_op.drop_column('image')
        batch_op.drop_column('confirmed_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('image', mysql.VARCHAR(length=150), nullable=True))
        batch_op.alter_column('image_filename',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=108),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
