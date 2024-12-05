"""
Add former limits to alert audit
"""

import sqlalchemy as sa
from alembic import op

revision = "19943ebcc90e"
down_revision = "4a2fa0837bf2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("alerts_log", sa.Column("trigger_upper_limit", sa.Float(), nullable=True))
    op.add_column("alerts_log", sa.Column("trigger_lower_limit", sa.Float(), nullable=True))
    op.drop_index("ix_physiological_alerts_code", table_name="alerts_log")
    op.drop_index("ix_physiological_alerts_device_code", table_name="alerts_log")
    op.drop_index("ix_physiological_alerts_patient_id", table_name="alerts_log")
    op.create_index(op.f("ix_alerts_log_code"), "alerts_log", ["code"], unique=False)
    op.create_index(op.f("ix_alerts_log_device_code"), "alerts_log", ["device_code"], unique=False)
    op.create_index(op.f("ix_alerts_log_patient_id"), "alerts_log", ["patient_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_alerts_log_patient_id"), table_name="alerts_log")
    op.drop_index(op.f("ix_alerts_log_device_code"), table_name="alerts_log")
    op.drop_index(op.f("ix_alerts_log_code"), table_name="alerts_log")
    op.create_index(
        "ix_physiological_alerts_patient_id", "alerts_log", ["patient_id"], unique=False
    )
    op.create_index(
        "ix_physiological_alerts_device_code", "alerts_log", ["device_code"], unique=False
    )
    op.create_index("ix_physiological_alerts_code", "alerts_log", ["code"], unique=False)
    op.drop_column("alerts_log", "trigger_lower_limit")
    op.drop_column("alerts_log", "trigger_upper_limit")
    # ### end Alembic commands ###