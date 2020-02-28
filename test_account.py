from datetime import date

from unittest import TestCase, skip
from unittest.mock import Mock, patch, call

from banking import Account


class TestAccount(TestCase):

    @patch('banking.date')
    @patch('banking.DepositTransaction')
    def test_deposit_adds_one_deposit_transaction(self, mock_transaction_constructor, mock_date):
        mock_transaction = mock_transaction_constructor.return_value
        mock_date.today.return_value = date(2012, 1, 10)
        mock_transaction_history = Mock()

        account = Account(transaction_history=mock_transaction_history)
        account.deposit(1000)

        mock_transaction_constructor.assert_called_with(1000, date(2012, 1, 10))
        mock_transaction_history.add.assert_called_with(mock_transaction)

    @patch('banking.date')
    @patch('banking.DepositTransaction')
    def test_deposit_adds_multiple_transactions(self, mock_transaction_constructor, mock_date):
        mock_transaction = mock_transaction_constructor.return_value
        mock_date.today.side_effect = [
            date(2012, 1, 10),
            date(2012, 1, 13)
        ]

        mock_transaction_history = Mock()
        account = Account(transaction_history=mock_transaction_history)

        account.deposit(1000)
        account.deposit(2000)

        mock_transaction_constructor.assert_has_calls(
            [
                call(1000, date(2012, 1, 10)),
                call(2000, date(2012, 1, 13))
            ]
        )

        mock_transaction_history.add.assert_has_calls(
            [
                call(mock_transaction),
                call(mock_transaction)
            ]
        )

    @patch('banking.date')
    @patch('banking.WithdrawTransaction')
    def test_withdraw_adds_one_withdraw_transactions(self, mock_transaction_constructor, mock_date):
        mock_transaction = mock_transaction_constructor.return_value
        mock_date.today.return_value = date(2012, 1, 14)

        mock_transaction_history = Mock()
        account = Account(transaction_history=mock_transaction_history)

        account.withdraw(500)

        mock_transaction_constructor.assert_called_with(500, date(2012, 1, 14))

        mock_transaction_history.add.assert_called_with(mock_transaction)

    @patch('banking.date')
    @patch('banking.DepositTransaction')
    @patch('banking.BankStatement')
    def test_print_statement_for_one_transaction(self,
            mock_bank_statement_constructor,
            mock_transaction_constructor,
            mock_date
            ):
        mock_transaction = mock_transaction_constructor.return_value
        mock_bank_statement = mock_bank_statement_constructor.return_value
        mock_date.today.return_value = date(2012, 1, 14)

        mock_output = Mock()
        mock_transaction_history = Mock()

        account = Account(transaction_history=mock_transaction_history, output=mock_output)

        account.deposit(500)
        account.print_statement()

        mock_bank_statement_constructor.assert_called_with(mock_transaction_history)
        mock_output.write.assert_called_with(str(mock_bank_statement))
