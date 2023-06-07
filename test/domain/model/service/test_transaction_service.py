from datetime import datetime
import uuid
from mock import MagicMock

from pytest import fixture

from domain.model.account import Account
from domain.model.transaction import Transaction, TransactionType
from domain.service.transaction_service import TransactionService


class TestTransactionService(object):
    @fixture
    def transaction_repository(self):
        return MagicMock()

    @fixture
    def account_repository(self):
        return MagicMock()

    @fixture
    def transaction_service(self, transaction_repository, account_repository):
        return TransactionService(transaction_repository, account_repository)

    def test_should_transfer_to_same_ownership(self, transaction_service, transaction_repository):
        amount = 100
        description = 'test description'
        checking = Account(id=1, account_number='123', branch_number='321', customer_document_number='123321', customer_name='gam', created_date=datetime.utcnow(), type='CHECKING')
        savings = Account(id=2, account_number='444', branch_number='321', customer_document_number='123321', customer_name='gam', created_date=datetime.utcnow(), type='SAVINGS')

        debit = Transaction(uuid.uuid4(), amount, description, datetime.now(), checking.id, None, None,
                            savings.account_number, savings.branch_number, TransactionType.DEBIT)

        credit = Transaction(uuid.uuid4(), amount, description, datetime.now(), savings.id, checking.account_number,
                             checking.branch_number, None, None, TransactionType.CREDIT)

        transaction_repository.load = MagicMock(return_value=checking)
        transaction_repository.load_by_account_number_and_branch = MagicMock(return_value=savings)

        transaction_service.transfer(1, amount, description, savings.account_number, savings.branch_number)
        transaction_repository.create_transactions.assert_called_once_with([debit, credit])

    def test_should_not_allowed_transfer_to_different_ownership(self, transaction_service, transaction_repository):
        amount = 100
        description = 'test description'
        savings = Account(id=1, account_number='123', branch_number='321', customer_document_number='123321', customer_name='gam', created_date=datetime.utcnow(), type='SAVINGS')
        checking = Account(id=2, account_number='444', branch_number='321', customer_document_number='400000', customer_name='joao', created_date=datetime.utcnow(), type='CHECKING')

        transaction_repository.load = MagicMock(return_value=checking)
        transaction_repository.load_by_account_number_and_branch = MagicMock(return_value=savings)

        try:
            transaction_service.transfer(1, amount, description, checking.account_number, checking.branch_number)
            assert False
        except Exception as e:
            assert str(e) == 'Cant transfer'    
