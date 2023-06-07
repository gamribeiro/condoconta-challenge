from domain.service.statement_service import StatementService
from datetime import datetime
import uuid
from mock import MagicMock

from pytest import fixture


class TestStatementService(object):

    @fixture
    def transaction_repository(self):
        return MagicMock()

    @fixture
    def transaction_service(self, transaction_repository):
        return StatementService(transaction_repository)

