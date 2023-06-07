from datetime import datetime

from pytest import fixture

from domain.model.account import Account
from domain.model.account_repository import AccountRepository
from test.integration_test import IntegrationTest


class TestAccountRepository(IntegrationTest):

    @fixture
    def transaction_repository(self):
        return AccountRepository()

    def test_should_load_account(self, transaction_repository, session):
        account = Account(id=1, account_number='123', branch_number='321', customer_document_number='123321', customer_name='gam', created_date=datetime.utcnow(), type='CHECKING')
        session.add(account)

        account = transaction_repository.load(1)
        assert account.id == account

