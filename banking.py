import sys
from datetime import date


class BankStatement:
    def __init__(self, transaction_history):
        self.transaction_history = transaction_history

    def __str__(self):
        header = 'Date|Credit|Debit|Balance\n'
        body = ''
        balance = 0

        for transaction in self.transaction_history.transactions():
            transaction_date = transaction.date.strftime('%d/%m/%Y')

            if isinstance(transaction, DepositTransaction):
                balance += transaction.amount
                body = "{}|{}||{}\n".format(transaction_date, transaction.amount, balance) + body
            else:
                balance -= transaction.amount
                body = "{}||{}|{}\n".format(transaction_date, transaction.amount, balance) + body

        return header + body


class Transaction:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date


class DepositTransaction(Transaction):
    pass


class WithdrawTransaction(Transaction):
    pass


class TransactionHistory:
    def __init__(self):
        self.history = []

    def add(self, transaction):
        self.history.append(transaction)

    def transactions(self):
        return self.history


class Account:
    def __init__(self, transaction_history=TransactionHistory(), output=sys.stdout):
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
        self.output.write(str(statement))
