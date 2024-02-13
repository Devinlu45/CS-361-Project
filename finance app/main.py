import pymongo
from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox
from tkinter import *

cluster = MongoClient("mongodb+srv://Devinlu1:Persona4golden@cluster0.7qs6qve.mongodb.net/")

db = cluster["Finances"]

collection = db["Banks"]

val1 = None
val2 = None
val3 = None
val4 = None

x = collection.find({})

for a in x:
    for b in a:
        if b == 'Checking Balance':
            val1 = a[b]
        elif b == 'Latest Deduction':
            val2 = a[b]
        elif b == 'Savings Balance':
            val3 = a[b]
        elif b == 'Interest Payments':
            val4 = a[b]
# Function to validate the login
            
root = tk.Tk()
root.title("Login Form")

username_label = tk.Label(root, text="User Name:")
username_label.pack()

userName_entry = tk.Entry(root)
userName_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="$") 
password_entry.pack()
def validate_login():
    userName = userName_entry.get()
    password = password_entry.get()

    if userName == "admin" and password == "password":
        messagebox.showinfo("Login worked", "You did it!")
        page_1()
    else:
        messagebox.showerror("Login didn't work", "wrong username or password")

def page_1():
    root = tk.Tk()
    title = Label(root, text="Checking and Savings Account")
    bank = Label(root, text = "Bank1")
    myLabel1 = Label(root, text = "Checking Account")
    myLabel2 = Label(root, text = "Saving Account")
    button = tk.Button(root, text="Checking info", command=doubleCheck)
    second_button = tk.Button(root, text = "Savings info", command = doubleCheck1)
    balance_1 = Label(root, text = val1)
    balance_2 = Label(root, text = val3)
    extensions = tk.Button(root, text="Additional Extensions", command = extensionPage)
    need_help = tk.Button(root, text = "click for help", command = helpdesk)

    myLabel1.grid(row=2, column=0)
    myLabel2.grid(row=3, column = 0)
    title.grid(row=0, column = 1)
    bank.grid(row = 1, column = 1)
    button.grid(row = 2, column = 4)
    second_button.grid(row=3, column = 4)
    balance_1.grid(row= 2, column = 3)
    balance_2.grid(row=3, column = 3)
    extensions.grid(row = 3, column = 5)
    need_help.grid(row = 3, column = 6)

    root.mainloop()

def page_2():
    root = tk.Tk()
    thing = Label(root, text="This is your checking balance")
    thing1 = Label(root, text="Checking Balance:")
    thing2 = Label(root, text = "Latest Deduction:")
    thing3 = Label(root, text = val1)
    thing4 = Label(root, text = val2)
    need_help = tk.Button(root, text = "click for help", command = helpdesk)

    thing.grid(row=0, column = 1)
    thing1.grid(row =1, column = 0)
    thing2.grid(row=2, column = 0)
    thing3.grid(row=1, column =2)
    thing4.grid(row=2, column = 2)
    need_help.grid(row = 2, column = 3)

    root.mainloop()

def page_3():
    root = Tk()
    another = Label(root, text="This is your savings balance")
    another_1 = Label(root, text = "Savings Balance:")
    another_2 = Label(root, text = "Interest Payments:")
    another_3 = Label(root, text = val3)
    another_4 = Label(root, text = val4)
    need_help = tk.Button(root, text = "click for help", command = helpdesk)
    another.grid(row=0, column = 1)
    another_1.grid(row =1, column = 0)
    another_2.grid(row=2, column = 0)
    another_3.grid(row=1, column =2)
    another_4.grid(row=2, column = 2)
    need_help.grid(row = 2, column = 3)
    root.mainloop()

def extensionPage():
    root = Tk()
    yay = Label(root, text = "Additional Extensions for the user")
    yay_1 = Label(root, text = 'new features:')
    yay_2 = Label(root, text = "old features:")
    yay_3 = tk.Checkbutton(root, text = 'Auto Sort Banks by lowest amounts(Recommended for more experienced users)', onvalue = 1, offvalue = 0)
    yay_4 = tk.Checkbutton(root, text = 'Basic buttons to check financials, nothing fancy (Recommended for the less tech savvy people)', onvalue = 1, offvalue=0)
    need_help = tk.Button(root, text = "click for help", command = helpdesk)
    yay.grid(row= 0, column = 1)
    yay_1.grid(row=1, column = 1)
    yay_2.grid(row=3, column = 1)
    yay_3.grid(row=2, column = 1)
    yay_4.grid(row=4, column = 1)
    need_help.grid(row = 4, column = 2)
    root.mainloop()

def doubleCheck():
    root = tk.Tk()
    something = Label(root, text = "Are you sure you want to check your checking?")
    something1 = tk.Button(root, text = "yes?", command = page_2)
    something2 = tk.Button(root, text = "No")
    something.grid(row = 0, column = 1)
    something1.grid(row = 1, column = 0)
    something2.grid(row = 1, column = 1)
    root.mainloop()

def doubleCheck1():
    root = tk.Tk()
    nothing = Label(root, text = "Are you sure you want to check your savings?")
    nothing1 = tk.Button(root, text = "Yes?", command = page_3)
    nothing2 = tk.Button(root, text = "No")
    nothing.grid(row = 0, column = 1)
    nothing1.grid(row= 1, column = 0)
    nothing2.grid(row = 1, column = 1)
    root.mainloop()
    
def helpdesk():
    root = tk.Tk()
    help = tk.Button(root, text = "Press this button to get connected to a live service representative")
    help1= tk.Button(root, text = "Need Help?")
    help.grid(row = 1, column = 0)
    help1.grid(row = 0, column = 0)

login_button = tk.Button(root, text="Press this button to login", command=validate_login)
login_button.pack()

root.mainloop()