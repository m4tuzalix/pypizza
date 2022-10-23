"""first migration

Revision ID: c4b082a94c19
Revises: 5fa57ebb3123
Create Date: 2022-10-23 16:38:44.310328

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c4b082a94c19"
down_revision = "5fa57ebb3123"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "pizza",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "price",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("ingredients", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name="pizza_pkey"),
        sa.UniqueConstraint("name", name="pizza_name_key"),
    )
    op.create_table(
        "orderhistory",
        sa.Column("order", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("date", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column(
            "status",
            postgresql.ENUM(
                "VERIFICATION",
                "ACCEPTED",
                "IN_PROGRESS",
                "IN_TRANSPORT",
                "DELIVERED",
                name="status",
            ),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('orderhistory_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["order"], ["order.id"], name="orderhistory_order_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="orderhistory_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "order",
        sa.Column(
            "pizzas",
            postgresql.ARRAY(postgresql.JSONB(astext_type=sa.Text())),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("surname", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("phone", sa.VARCHAR(length=9), autoincrement=False, nullable=False),
        sa.Column(
            "postal_code", sa.VARCHAR(length=6), autoincrement=False, nullable=False
        ),
        sa.Column("address", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("active", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("date", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column("history", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["history"], ["orderhistory.id"], name="order_history_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="order_pkey"),
    )


def downgrade() -> None:
    op.drop_constraint(constraint_name="pizza_name_key", table_name="pizza")
    op.drop_constraint(constraint_name="pizza_pkey", table_name="pizza")
    op.drop_constraint(
        constraint_name="orderhistory_order_fkey", table_name="orderhistory"
    )
    op.drop_constraint(constraint_name="order_history_fkey", table_name="order")
    op.drop_constraint(constraint_name="order_pkey", table_name="order")
    op.drop_constraint(constraint_name="orderhistory_pkey", table_name="orderhistory")
    op.drop_table("pizza")
    op.drop_table("order")
    op.drop_table("orderhistory")
