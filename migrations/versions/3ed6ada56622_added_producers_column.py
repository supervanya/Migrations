"""added producers column

Revision ID: 3ed6ada56622
Revises: dfd7e7528211
Create Date: 2018-11-02 13:22:46.673902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ed6ada56622'
down_revision = 'dfd7e7528211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('albums', sa.Column('producers', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('albums', 'producers')
    # ### end Alembic commands ###
