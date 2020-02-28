from unittest import TestCase
from datetime import date

from banking import DepositTransaction, TransactionHistory


class TestTransactionHistory(TestCase):
    def test_with_one_transaction(self):
        transaction = DepositTransaction(1000, date(2020, 1, 1))

        transaction_history = TransactionHistory()
        transaction_history.add(transaction)

        self.assertIn(transaction, transaction_history.transactions())
