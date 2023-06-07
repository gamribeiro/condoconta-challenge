from enum import Enum


class TransactionType(Enum):
    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'


class Transaction:
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