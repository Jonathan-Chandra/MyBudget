from tkinter import *
from tkinter import ttk

myBudgetInstance = Tk()


def init():
    myBudgetInstance.title("MyBudget")
    myBudgetInstance.geometry('1920x1080')
    myBudgetInstance.configure(background='white')
    myBudgetInstance.mainloop()
    return 0
