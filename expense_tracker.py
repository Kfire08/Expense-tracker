from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="admin",database="expense")
mycursor=mydb.cursor()
mycursor.execute("Select * from record")
result=mycursor.fetchall()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def submit():
    if entry2.get()=='' or entry3.get()=='' or is_number(entry3.get())==False:
        messagebox.showinfo('','Enter valid values')
    else:
        date = entry1.get()
        month = date[:2]
        day = date[3:5]
        year = date[6:]
        date = '20' + year + '-' + month + '-' + day
        print(date)
        title = entry2.get()
        expense = entry3.get()
        data = [date,title,expense]
        print(data)
        query = "insert into record values('" + date + "', '" + title + "', " + expense + ");"
        print(query)
        mycursor.execute(query)
        box.insert('','end',values=data)
        mydb.commit()
root = Tk()
root.geometry('615x420')
label1 = Label(text='Date',font=('Times New Roman',24))
entry1 = DateEntry(width=19, background='blue' ,foreground='white',font=(None,18))
label2 = Label(text='Title',font=('Times New Roman',24))
entry2 = Entry(font=('Times New Roman',24))
label3 = Label(text='Expense',font=('Times New Roman',24))
entry3 = Entry(font=('Times New Roman',24))
button = Button(text='Submit',font=('Times New Roman',24),bg='white',fg='brown',command=submit)
headings = ['Date' , 'Title' ,'Expense']
box = ttk.Treeview(root, column= headings, show='headings',height=5)
for i in headings:
	box.heading(i, text=i.title())
label1.grid(row=0, column=0, padx=5, pady=5,sticky='W')
label2.grid(row=1, column=0, padx=5, pady=5,sticky='W')
label3.grid(row=2, column=0, padx=5, pady=5,sticky='W')
entry1.grid(row=0, column=1, padx=5, pady=5,sticky='W')
entry2.grid(row=1, column=1, padx=5, pady=5,sticky='W')
entry3.grid(row=2, column=1, padx=5, pady=5,sticky='W')
button.grid(row=3, column=1, padx=5, pady=5,sticky='W', columnspan=3)
box.grid(row=4, column=0, padx=5, pady=5,sticky='W',columnspan=3)

for x in result:
    x = list(x)
    box.insert('','end',values=x)

root.title('Expense Tracker')
root.mainloop()