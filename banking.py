import sys
from datetime import date


class BankStatement:
    def __init__(self, transaction_history):
        pass


class DepositTransaction:
    def __init__(self, amount, date):
        pass


class WithdrawTransaction:
    def __init__(self, amount, date):
        pass


class Account:
    def __init__(self, transaction_history, output=sys.stdout):
        self.output = output
        self.transaction_history = transaction_history

    def deposit(self, amount):
        transaction = DepositTransaction(amount, date.today())
        self.transaction_history.add(transaction)

    def withdraw(self, amount):
        transaction = WithdrawTransaction(amount, date.today())
        self.transaction_history.add(transaction)

    def print_statement(self):
        statement = BankStatement(self.transaction_history)
        self.output.write(statement)
