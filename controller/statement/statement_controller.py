from controller import app
from domain.service.statement_service import StatementService
from flask import request


@app.route('/statement', methods=['GET'])
def get_statement():
    response = StatementService().load_statement_by_account(request.args.get('account_id'), request.args.get('start_date'), request.args.get('end_date'))