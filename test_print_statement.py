import io
from datetime import date

from unittest import TestCase, skip
from unittest.mock import patch

from banking import Account


class TestPrintStatement(TestCase):

    @patch('banking.date')
    def test_print_statement(self, mock_date):
        mock_date.today.side_effect = [
            date(2012, 1, 10),
            date(2012, 1, 13),
            date(2012, 1, 14)
        ]

        output = io.StringIO()
        account = Account(output=output)

        account.deposit(1000)
        account.deposit(2000)
        account.withdraw(500)
        account.print_statement()

        self.assertEqual(
'''\
Date|Credit|Debit|Balance
14/01/2012|500||2500
13/01/2012||2000|3000
10/01/2012||1000|1000
''',
            output.getvalue()
        )
