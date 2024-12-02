"""
Adds unique constrain to primary_identifier
"""

from alembic import op

revision = "591e3588e42f"
down_revision = "7d5f51ecdcb6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "patients", ["primary_identifier"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "patients", type_="unique")
    # ### end Alembic commands ###
