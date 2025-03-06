"""Added User model

Revision ID: 5009a4d52fb8
Revises: 49e1ab6b3dde
Create Date: 2025-03-06 00:35:53.589663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5009a4d52fb8'
down_revision = '49e1ab6b3dde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
