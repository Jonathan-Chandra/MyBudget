import datetime
from Models.Accounts.Account import Account


class Budget:
    def __init__(self, name, category, balance, account_stored: Account, end_date: datetime):
        self.name = name
        self.category = category
        self.balance = balance
        assert isinstance(account_stored, Account)
        self.account_stored = account_stored
        assert isinstance(end_date, datetime)
        self.end_date = end_date
