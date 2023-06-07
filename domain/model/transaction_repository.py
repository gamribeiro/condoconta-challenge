from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy_utils import UUIDType

from domain.model.transaction import Transaction, TransactionType
from infrastructure.database.connection_factory import Base, Session


class TransactionRepository:
    def __init__(self, session=None):
        self.session = session or Session()

    def load_balance_after_transaction(self, transaction):
        balance_query = self.session.query(func.sum(
            func.case([(TransactionTable.type == 'CREDIT', TransactionTable.amount)],
                      else_=TransactionTable.amount * -1)
        )).filter(TransactionTable.created_date <= transaction.created_date)\
            .filter(TransactionTable.from_account_number == transaction.from_account_number)\
            .filter(TransactionTable.from_account_branch == transaction.from_account_branch)\

        return balance_query.scalar()

    def list_by_account_and_dates(self, account_id, start_date, end_date):
        transactions = self.session.query(TransactionTable).filter(TransactionTable.created_date >= start_date)\
            .filter(TransactionTable.created_date <= end_date)\
            .filter(TransactionTable.account_id == account_id)\
            .all()
        return [transaction.to_domain() for transaction in transactions]


class TransactionTable(Base):
    __tablename__ = "transactions"
    id = Column(UUIDType(), primary_key=True)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    account_id = Column(UUIDType(), primary_key=True)
    from_account_number = Column(String, nullable=False)
    from_account_branch = Column(String, nullable=False)
    to_account_number = Column(String, nullable=False)
    to_account_branch = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __init__(self, id, amount, description, created_date, account_id, from_account_number, from_account_branch,
                 to_account_number, to_account_branch, type):
        self.id = id
        self.amount = amount
        self.description = description
        self.created_date = created_date
        self.account_id = account_id
        self.from_account_number = from_account_number
        self.from_account_branch = from_account_branch
        self.to_account_number = to_account_number
        self.to_account_branch = to_account_branch
        self.type = type

    def to_domain(self):
        return Transaction(id=self.id, amount=self.amount, description=self.description, created_date=self.created_date, account_id=self.account_id,
                           from_account_number=self.from_account_number, from_account_branch=self.from_account_branch,
                           to_account_number=self.to_account_number, to_account_branch=self.to_account_branch, type=TransactionType(self.type))
    @staticmethod
    def to_table(transaction):
        return TransactionTable(
            id=transaction.id,
            amount=transaction.amount,
            description=transaction.description,
            created_date=transaction.created_date,
            account_id=transaction.account_id,
            from_account_number=transaction.from_account_number,
            from_account_branch=transaction.from_account_branch,
            to_account_number=transaction.to_account_number,
            to_account_branch=transaction.to_account_branch,
            type=transaction.type.value)