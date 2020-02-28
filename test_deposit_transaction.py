from datetime import date
from unittest import TestCase

from banking import DepositTransaction


class TestDepositTransaction(TestCase):
    def test_has_amount(self):
        transaction = DepositTransaction(1000, date(2020, 1, 1))
        self.assertEqual(transaction.amount, 1000)

    def test_has_date(self):
        transaction = DepositTransaction(1000, date(2020, 1, 1))
        self.assertEqual(transaction.date, date(2020, 1, 1))
