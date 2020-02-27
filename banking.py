import sys


class Account:
    def __init__(self, output=sys.stdout):
        self.output = output

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def print_statement(self):
        self.output.write('changeme')
