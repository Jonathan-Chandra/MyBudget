from Models.Accounts.Account import Account
from Models.Accounts.Goals import Goal
import datetime


class Transactions:
    def __init__(self, name, amount, date_of_transaction: datetime, account: Account, category, goal: Goal):
        self.name = name
        self.amount = amount
        assert isinstance(date_of_transaction, datetime)
        self.date_of_transaction = date_of_transaction
        assert isinstance(account, Account)
        self.account = account
        self.category = category
        assert isinstance(goal, Goal)
        self.goal = goal
