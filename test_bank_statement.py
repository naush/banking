from datetime import date
from unittest import TestCase
from unittest.mock import Mock

from banking import BankStatement, DepositTransaction, WithdrawTransaction


class TestBankStatement(TestCase):
    def test_no_transaction(self):
        mock_transaction_history = Mock()
        mock_transaction_history.transactions.return_value = []
        statement = BankStatement(mock_transaction_history)
        self.assertEqual(statement.__str__(),
'''\
Date|Credit|Debit|Balance
'''
        )

    def test_one_deposit_transaction(self):
        mock_transaction_history = Mock()
        mock_transaction_history.transactions.return_value = [
            DepositTransaction(1000, date(2020, 1, 1))
        ]
        statement = BankStatement(mock_transaction_history)
        self.assertEqual(statement.__str__(),
'''\
Date|Credit|Debit|Balance
01/01/2020||1000|1000
'''
        )

    def test_one_withdraw_transaction(self):
        mock_transaction_history = Mock()
        mock_transaction_history.transactions.return_value = [
            DepositTransaction(1000, date(2020, 1, 1)),
            WithdrawTransaction(500, date(2020, 1, 2))
        ]
        statement = BankStatement(mock_transaction_history)
        self.assertEqual(statement.__str__(),
'''\
Date|Credit|Debit|Balance
02/01/2020|500||500
01/01/2020||1000|1000
'''
        )
