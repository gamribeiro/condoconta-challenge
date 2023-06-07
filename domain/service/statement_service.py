from domain.model.statement import StatementTransaction, Statement


class StatementService:
    def __init__(self, transaction_repository):
        self.transaction_repository = transaction_repository

    def load_statement_by_account(self, account_id, start_date, end_date):
        transactions = self.transaction_repository.list_by_account(account_id, start_date, end_date)

        statement_transactions = [StatementTransaction(transaction, self.transaction_repository.load_balance_after_transaction(transaction))
                                  for transaction in transactions]
        return Statement(statement_transactions)