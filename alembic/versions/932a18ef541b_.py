"""empty message

Revision ID: 932a18ef541b
Revises: 3bfd9efe2ce1
Create Date: 2022-03-14 18:15:55.396893

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "932a18ef541b"
down_revision = "3bfd9efe2ce1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("is_superuser", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_superuser")
    # ### end Alembic commands ###
