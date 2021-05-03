from Models.Accounts import Account
from Models.Budget import Budget
from Models.Goals.Goal import Goal


class User:
    accounts = list[Account]
    goals = list[Goal]
    budgets = list[Budget]

    def __init__(self, first_name, last_name, accounts: list[Account], goals: list[Goal], budgets: list[Budget]):
        self.firstName = first_name
        self.lastName = first_name
        self.accounts = accounts
        self.goals = goals
        assert isinstance(budgets, list(Budget))
        self.budgets = budgets

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_account(self, account):
        self.accounts.append(account)

    def add_budget(self, budget):
        self.budgets.append(budget)
