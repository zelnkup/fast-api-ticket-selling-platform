"""empty message

Revision ID: 682c0fb6f748
Revises: b2154323fe04
Create Date: 2022-03-08 20:47:59.551917

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "682c0fb6f748"
down_revision = "b2154323fe04"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("salt", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "salt")
    # ### end Alembic commands ###
