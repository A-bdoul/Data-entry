import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql



window = tkinter.Tk()
window.title("Login Form")
window.geometry('500x600')
window.configure(bg='dodgerBlue4')


def login():
    if username_entry.get() == '':
        messagebox.showerror('Alert', 'Please enter your email')
    elif password_entry.get() == '':
        messagebox.showerror(('Alert', 'Please enter your password'))
    else:
        db = pymysql.connect(host='localhost', user='root', password='H@nane10', database='my_account')
        cur = db.cursor()
        query = 'select * from p_details where password=%s'
        cur.execute(query, (password_entry.get()))

        row = cur.fetchone()
        if row == None:
            messagebox.showerror('Alert', 'Incorrect username')
            return
        else:
            messagebox.showinfo('Success', 'Successfully Login')

        window.destroy()
        import Home_page

def create_account():
    window.destroy()
    import create_account



frame = tkinter.Frame(bg='dodgerBlue4')

# label = tkinter.Label(window, text = "Login" )
# label.grid(row=0, column= 1)

# Creating widgets
login_label = tkinter.Label(frame, text=" Welcome to Track Expense", bg='dodgerBlue4', fg="white", font=("Comic Sans MS", 15))
username_label = tkinter.Label(frame, text="Username", bg='dodgerBlue4', fg="white", font=("Arial", 10))
username_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password", bg='dodgerBlue4', fg="white", font=("Arial", 10))
login_button = tkinter.Button(frame, text="Login", font=("Arial", 12), bg="green", fg="white", command=login)
dont_have_account_label = tkinter.Label(frame, text="don't have an account?",bg= 'dodgerBlue4', font= ("Comic Sans MS", 10), fg="white", )
dont_have_account_button = tkinter.Button(frame, text ="Create Account", bg= 'red', font=("Arial",10), fg= "white", command=create_account)

# Placing username and password widget

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=10)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
dont_have_account_label.grid(row = 4, column=0, columnspan= 10, pady=20)
dont_have_account_button.grid(row = 5, column= 0, columnspan= 10, pady=0)
frame.pack()

window.mainloop()
