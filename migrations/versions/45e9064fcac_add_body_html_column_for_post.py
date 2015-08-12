"""add body_html column for Post

Revision ID: 45e9064fcac
Revises: 7c2ccb3e2d
Create Date: 2015-08-12 00:38:52.795449

"""

# revision identifiers, used by Alembic.
revision = '45e9064fcac'
down_revision = '7c2ccb3e2d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###