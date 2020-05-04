from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.geometry('300x300')
label1 = Label(text='Username', font=('Times New Roman',24))
entry1 = Entry(font=('Times New Roman',24))
label2 = Label(text='Password', font=('Times New Roman',24))
entry2 = Entry(font=('Times New Roman',24), show='*')
def login():
    if entry1.get()=='' or entry2.get()=='':
        messagebox.showinfo('','Please Enter the details Correctly')
    else:
        username = entry1.get()
        password = entry2.get()
        if (username == 'Aditya' and password == 'Aditya1510') or (username == 'akash' and password == 'akashk08') or (username == 'Nikhil' and password == 'Nikk'):
            os.system('start expense_tracker.py')
            root.destroy()
        else:
            messagebox.showinfo('','Please Enter the details Correctly')
button = Button(text='Login', font=('Times New Roman',24),command=login)
label1.pack(pady=5)
entry1.pack(pady=5)
label2.pack(pady=5)
entry2.pack(pady=5)
button.pack(pady=5)
root.title('Login')
root.mainloop()
