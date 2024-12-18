"""
Mark unit code as optional
"""

import sqlalchemy as sa
from alembic import op

revision = "5c7fa9e062f8"
down_revision = "b57d01bc3b4e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("new_vitals", "unit_code", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("new_vitals", "unit_code", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
