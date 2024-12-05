"""
initializing-audit-table
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "c2f8dca5ec51"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "internal_audit",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("entity_id", sa.String(length=255), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("data", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("char_length(entity_id) > 0", name="entity_id_min_len"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_internal_audit_entity_id"),
        "internal_audit",
        ["entity_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_internal_audit_timestamp"),
        "internal_audit",
        ["timestamp"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_internal_audit_timestamp"), table_name="internal_audit")
    op.drop_index(op.f("ix_internal_audit_entity_id"), table_name="internal_audit")
    op.drop_table("internal_audit")
    # ### end Alembic commands ###