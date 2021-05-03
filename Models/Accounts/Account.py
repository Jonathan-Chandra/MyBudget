from Transactions import Transactions
import datetime


class Account:
    transactions = list([Transactions])

    def __init__(self, name, balance, transactions: list[Transactions]):
        self.name = name
        self.balance = balance
        assert isinstance(list([Transactions]))
        self.transactions = transactions


class CreditCardAccount(Account):
    def __init__(self, name, interest, statement_period, statement_end_date: datetime, balance, minimum_payment_amount,
                 transactions:
                 list[Transactions]):
        super().__init__(name, balance, transactions)
        self.interest = interest
        self.statement_period = statement_period
        self.minimum_payment_amount = minimum_payment_amount


class CheckingAccount(Account):
    pass


class SavingsAccount(Account):
    def __init__(self, name, interest, statement_period, balance, transactions):
        super().__init__(name, balance, transactions)
        self.interest = interest
        self.statement_period = statement_period

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
