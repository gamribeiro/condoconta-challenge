"""initial

Revision ID: 72dc4b52ace2
Revises: 
Create Date: 2023-06-07 15:22:09.411712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy_utils import UUIDType

revision = '72dc4b52ace2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "accounts",
        sa.Column("id", UUIDType(), nullable=False, primary_key=True),
        sa.Column("customer_name", sa.String(), nullable=False),
        sa.Column("customer_document_number", sa.String(), nullable=False),
        sa.Column("account_branch", sa.String(), nullable=False),
        sa.Column("account_number", sa.String(), nullable=False),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
    )

    op.create_table(
        "transactions",
        sa.Column("id", UUIDType(), nullable=False, primary_key=True),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("account_id", UUIDType(), nullable=False, primary_key=True),
        sa.Column("from_account_number", sa.String(), nullable=False),
        sa.Column("from_account_branch", sa.String(), nullable=False),
        sa.Column("to_account_number", sa.String(), nullable=False),
        sa.Column("to_account_branch", sa.String(), nullable=False),
        sa.Column("created_date", sa.DateTime(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
    )

    op.execute(
        """
        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'João', '12345678900', '0001', '0000001', '2023-06-07 15:00:38.368589', 'CHECKING');

        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'João', '12345678900', '0002', '0000001', '2023-06-07 15:00:38.368589', 'SAVINGS');

        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'jose', '12345644444', '0003', '0000001', '2023-06-07 15:00:38.368589', 'CHECKING');

        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'jose', '12345644444', '0004', '0000001', '2023-06-07 15:00:38.368589', 'SAVINGS');

        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'juliana', '12345644445', '0005', '0000001', '2023-06-07 15:00:38.368589', 'CHECKING');

        insert into accont (id, customer_name, customer_document_number, account_branch, account_number, created_date, type) 
        values (uuid_generate_v4(), 'maria', '12345644445', '0005', '0000001', '2023-06-07 15:00:38.368589', 'CHECKING');
        """
    )


def downgrade() -> None:
    op.drop_table("account")
    op.drop_table("transaction")
