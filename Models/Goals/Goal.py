import datetime
from Models.Accounts import Account


class Goal:
    def __init__(self, final_goal, end_date: datetime, current_balance, category, account_location: Account):
        self.final_goal = final_goal
        assert isinstance(end_date, datetime)
        self.end_date = end_date
        self.current_balance = current_balance
        self.category = category
        assert isinstance(account_location, Account)
        self.account_location = account_location
