from controller import app
from domain.service.transaction_service import TransactionService


@app.route('/transaction', methods=['POST'])
def transfer(transaction):
    transaction_service = TransactionService()
    return transaction_service.transfer(transaction.get('account_id'), transaction.get('amount'), transaction.get('description'), transaction.get('to_account_number'), transaction.get('to_account_branch'))