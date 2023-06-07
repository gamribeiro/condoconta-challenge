from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy_utils import UUIDType
from domain.model.account import Account, AccountType
from infrastructure.database.connection_factory import Base, Session


class AccountRepository:
    def __init__(self, session=None):
        self.session = session or Session()

    def load(self, account_id):
        account_table = self.session.query(AccountTable).filter(AccountTable.id == account_id).first()
        return account_table.to_domain()

    def load_by_account_number_and_branch(self, account_number, branch_number):
        account_table = self.session.query(AccountTable).filter(AccountTable.account_number == account_number).filter(AccountTable.account_branch == branch_number).first()
        return account_table.to_domain()


class AccountTable(Base):
    __tablename__ = "account"
    id = Column(UUIDType(), primary_key=True)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    from_account_number = Column(String, nullable=False)
    from_account_branch = Column(String, nullable=False)
    to_account_number = Column(String, nullable=False)
    to_account_branch = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __init__(self, id, account_number, branch_number, customer_name, customer_document_number, created_date, type):
        self.id = id
        self.account_number = account_number
        self.branch_number = branch_number
        self.customer_name = customer_name
        self.customer_document_number = customer_document_number
        self.created_date = created_date
        self.type = type

    def to_domain(self):
        return Account(id=self.id, account_number=self.account_number, branch_number=self.branch_number, customer_name=self.customer_name,
                       customer_document_number=self.customer_document_number, created_date=self.created_date, type=AccountType(self.type))

    @staticmethod
    def to_table(account):
        return AccountTable(
            id=account.id,
            account_number=account.account_number,
            branch_number=account.branch_number,
            customer_name=account.customer_name,
            customer_document_number=account.customer_document_number,
            created_date=account.created_date if account.created_date else datetime.utcnow(),
            type=account.type)