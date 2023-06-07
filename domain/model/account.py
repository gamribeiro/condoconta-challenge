from enum import Enum


class AccountType(Enum):
    CHECKING = 'CHECKING'
    SAVINGS = 'SAVINGS'


class Account:
    def __init__(self, id, customer_name, account_number, branch_number, customer_document_number, created_date, type):
        self.id = id
        self.account_number = account_number
        self.branch_number = branch_number
        self.customer_name = customer_name
        self.customer_document_number = customer_document_number
        self.created_date = created_date
        self.type = type

