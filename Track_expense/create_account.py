import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

#windows size
windows = Tk()
windows.title("Create My account")
windows.geometry('400x300')
windows.configure(bg='black')

#Database section
def submit():
    if username_entry.get() == '':
        messagebox.showinfo('Alert!', 'Please enter your username')
    elif password_entry.get() =='':
        messagebox.showinfo('Alert', 'Please enter your Password')

    else:
        db = pymysql.connect(host='localhost', user='root', password='H@nane10', database='my_account')
        cur = db.cursor()
        try:
                query = 'create database my_account'
                cur.execute(query)
                query = 'use my_account'
                cur.execute(query)
                # messagebox.showinfo('Nice Done','successful connected')
                # print('worked')

                query = 'create table P_details(id int auto_increment primary key not null, username varchar(40), password varchar(40))'

                cur.execute(query)
                messagebox.showinfo(('Success', 'field created'))

        except:
            cur.execute('use my_account')
            query = 'insert into P_details(username, password) values(%s,%s)'
            cur.execute(query,(username_entry.get() , password_entry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Successfully Registered')



frame = tkinter.Frame(bg= 'black')

username_label = tkinter.Label(frame, text="Username", bg='black', fg="white", font=("Arial", 10))
username_entry = tkinter.Entry(frame)
submit_button = tkinter.Button(frame, text = "Submit", bg= 'green', fg = 'white', font=("Arial", 10), command = submit)
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password", bg='black', fg="white", font=("Arial", 10))
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
submit_button.grid(row=3, column=1, pady=20)

frame.pack()


windows.mainloop()


