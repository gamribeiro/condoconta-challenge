class Statement:
    def __init__(self, statement_transactions):
        self.statement_transactions = statement_transactions


class StatementTransaction:
    def __init__(self, transaction, account_balance):
        self.transaction = transaction
        self.account_balance = account_balance
