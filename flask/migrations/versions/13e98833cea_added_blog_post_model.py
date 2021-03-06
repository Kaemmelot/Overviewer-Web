"""added blog post model

Revision ID: 13e98833cea
Revises: 3fa7c3b1be1
Create Date: 2015-03-25 19:55:45.927103

"""

# revision identifiers, used by Alembic.
revision = '13e98833cea'
down_revision = '3fa7c3b1be1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('published', sa.Boolean(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('slug', sa.String(length=128), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_post_slug'), 'blog_post', ['slug'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_post_slug'), table_name='blog_post')
    op.drop_table('blog_post')
    ### end Alembic commands ###
