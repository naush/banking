import io
from unittest import TestCase

from banking import Account


class TestPrintStatement(TestCase):
    def test_print_statement(self):
        output = io.StringIO()
        account = Account(output)

        account.deposit(1000)
        account.deposit(2000)
        account.withdraw(500)
        account.print_statement()

        self.assertEqual(
'''\
Date|Credit|Debit|Balance
14/01/2012||500|2500
13/01/2012|2000||3000
10/01/2012|1000||1000\
''',
            output.getvalue()
        )
