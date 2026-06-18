import pytest
from src.handlers.transaction_handler import handle_transaction
from src.models.transaction_model import Transaction

def test_handle_transaction():
    data = {'id': '1', 'amount': 100.0, 'currency': 'USD', 'status': 'pending'}
    transaction = handle_transaction(data)
    assert isinstance(transaction, Transaction)
    assert transaction.id == '1'
    assert transaction.amount == 100.0
    assert transaction.currency == 'USD'
    assert transaction.status == 'pending'