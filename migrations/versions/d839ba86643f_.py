"""empty message

Revision ID: d839ba86643f
Revises: 1355c9ece058
Create Date: 2020-06-12 22:32:54.307843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd839ba86643f'
down_revision = '1355c9ece058'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note',
    sa.Column('nid', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('nid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    # ### end Alembic commands ###
