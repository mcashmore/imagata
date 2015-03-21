"""Create Image and Tag tables

Revision ID: 42b363862751
Revises: 
Create Date: 2015-03-21 09:39:11.303000

"""

# revision identifiers, used by Alembic.
revision = '42b363862751'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(): 
    op.create_table(
        'image',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String),
        sa.Column('category', sa.String, nullable=False),
        sa.Column('subcategory', sa.String),
        sa.Column('filename', sa.String, nullable=False, unique=True),
        sa.Column('author', sa.String),
        sa.Column('source', sa.String),
        sa.Column('description', sa.Text),
    )
    
    op.create_table(
        'tag',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('image_id', sa.Integer, sa.ForeignKey('image.id')),
    )


def downgrade():
    op.drop_table('tag')
    op.drop_table('image')
