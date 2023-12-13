import tkinter
from tkinter import ttk
from tkinter import messagebox
import os

# import filepath as filepath
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import openpyxl

file_path = r"C:\Users\abdou\OneDrive\Desktop\project\Track_expense\Book1.xlsx"
A = openpyxl.load_workbook((file_path))
B = A["Data"]

def enter_data():
    date = date_entry.get()
    revenue = revenue_entry.get()
    expense = expense_entry.get()

    kind = type_combobox.get()
    if date and revenue and expense and kind:
        B.append([date, revenue, expense, kind])
        A.save(file_path)
        messagebox.showinfo("Status", "Data saved")
    else:
        messagebox.showwarning("Warning", "Data not saved")

    # print("Date: ", date, "revenue:", revenue, "expense:", expense, "type_expense", kind)

def calculate_profit():
    revenue = float(revenue_entry.get())
    expense = float(expense_entry.get())
    profit = (revenue - expense)

    profit_label.config(text= f'Profit: ${profit:2f}')






window = tkinter.Tk()
window.title('Data Entry form')

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="Data Entry")
user_info_frame.grid(row=0, column=0, padx=10, pady=10)

# Date widget
date_label = tkinter.Label(user_info_frame, text="Date")
date_label.grid(row=0, column=0)
date_entry = tkinter.Entry(user_info_frame)
date_entry.grid(row=1, column=0)

# Revenue widget
revenue_label = tkinter.Label(user_info_frame, text="Revenue")
revenue_label.grid(row=0, column=1)
revenue_entry = tkinter.Entry(user_info_frame)
revenue_entry.grid(row=1, column=1)



# Expenses widget
expense_label = tkinter.Label(user_info_frame, text="Expense")
expense_label.grid(row=0, column=2)
expense_entry = tkinter.Entry(user_info_frame)
expense_entry.grid(row=1, column=2)

# Type of expense
type_label = tkinter.Label(user_info_frame, text="Type expense")
type_combobox = ttk.Combobox(user_info_frame, values=['', 'Gas', 'Food', 'Miscellaneous'])
type_label.grid(row=0, column=4)
type_combobox.grid(row=1, column=4)

# Profit widget
profit_label = tkinter.LabelFrame(user_info_frame, text='Profit')
profit_label.grid(row=0, column=3)
#profit_frame = tkinter.Label(user_info_frame)
#profit_frame.grid(row =1, column=3)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=4,column=0, sticky="news", padx=20, pady=20)

calculate_button = tkinter.Button(frame, text= "Calculate Profit", command=calculate_profit)
calculate_button.grid(row=3, column=0, sticky="news", padx=20, pady= 20)
window.mainloop()
