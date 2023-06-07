import uuid
from datetime import datetime

from domain.model.account_repository import AccountRepository
from domain.model.transaction import Transaction, TransactionType
from domain.model.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, transaction_repository, account_repository):
        self.transaction_repository = transaction_repository or TransactionRepository()
        self.account_repository = account_repository or AccountRepository()

    def transfer(self, account_id, amount, description, to_account_number, to_account_branch):
        account = self.account_repository.load(account_id)
        to_account = self.account_repository.load_by_account_number_and_branch(to_account_number, to_account_branch)

        if account.customer_document_number == to_account.customer_document_number:
            debit = Transaction(uuid.uuid4(), amount, description, datetime.now(), account.id, None, None, to_account_number,
                                to_account_branch, TransactionType.DEBIT)

            credit = Transaction(uuid.uuid4(), amount, description, datetime.now(), to_account.id, account.account_number, account.account_branch,
                                None, None, TransactionType.CREDIT)

            self.transaction_repository.create_transactions([debit, credit])
        else:
            raise Exception("Cant transfer")
