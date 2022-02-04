
"""
/****************************************************************
*                                                               *
* Date:                                                         *
* Developer: ???????????                                        *
* Appliction: Stipend.Python                                    *
*                                                               *
* Description: Application to Post Stipends Earned and Deducted *
*              To an SQLite Database file                       *
*                                                               *
****************************************************************/
"""

from tkinter import *
from tkinter import ttk
import sqlite3

##################  #########################

# Connect to Database
def create_connection(pathToDataBase):
    connection = None
    try:
        connection = sqlite3.connect(pathToDataBase)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        return false

def execute_read_query(connection, query):
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


######################### SQL CREATE TABLE SECTION ###################################


######################### SQL + PYTHON SECTION ###################################
        
def post(*args):
    try:
        
        profile = (name.get(),day.get(),assignment.get(),credit.get(), debit.get(),comment.get())
        cursor.execute("INSERT into stipends(name,day,assignment,credit,debit,comment) values (?,?,?,?,?,?)", profile)
        
        connection.commit()
        cursor.close

    except ValueError:
        pass
    
    empty_fields()

###########################################################
################ TKINTER WINDOW SECTION ###################
###########################################################
    
#ROOT Setup
root = Tk()
root.title("STIPENDS")
root.resizable(False, False)

#MainFrame Window 
window = ttk.Frame(root, padding="3 3 12 12", width=400, height=250)
window.grid(column=0, row=0, sticky=(N, W, E, S))

#Inconveniencing piece of code
connection = create_connection('Final_Project.db')
cursor = connection.cursor() #represents the db connection


#Input Variables
name_var = StringVar()
day_var = StringVar()
assignment_var = StringVar()
credit_var = StringVar()
debit_var = StringVar()
comment_var = StringVar()

#Input Fields[Left Side]
name_lbl = ttk.Label(window, text="Name: ")
name_lbl.grid(column=1, row=0, sticky=W)
name = ttk.Entry(window, textvariable=name_var)
name.grid(column=1, row=1, sticky='we',columnspan=3)

day_lbl = ttk.Label(window, text="Date")
day_lbl.grid(column=1, row=2, sticky=W)
day = ttk.Entry(window, textvariable=day_var)
day.grid(column=1, row=3, sticky='we', columnspan=3)


assignment_lbl = ttk.Label(window, text="Assignment: ")
assignment_lbl.grid(column=1, row=4, sticky=W)
assignment = ttk.Entry(window, textvariable=assignment_var)
assignment.grid(column=1, row=5, sticky='we', columnspan=3)

credit_lbl = ttk.Label(window, text="Credit: ")
credit_lbl.grid(column=1, row=6, sticky=W)
credit = ttk.Entry(window, textvariable=credit_var, width=15)
credit.grid(column=1, row=7, sticky='we', columnspan=2)

debit_lbl = ttk.Label(window, text="debit: ")
debit_lbl.grid(column=1, row=8, sticky=W)
debit = ttk.Entry(window, textvariable=debit_var, width=3)
debit.grid(column=1, row=9, sticky='we',columnspan=3)

comment_lbl = ttk.Label(window, text="Comment: ")
comment_lbl.grid(column=1, row=10, sticky=W)
comment = ttk.Entry(window, textvariable=comment_var, width=3)
comment.grid(column=1, row=11, sticky='we',columnspan=3)

#Buttons
post_btn = ttk.Button(window, text="POST", command=post, width=12)
post_btn.grid(column=1, row=12, sticky='we')

update_btn = ttk.Button(window, text="UPDATE", command='', width=12)
update_btn.grid(column=3, row=12, sticky='W')





def empty_fields():
    name.delete(0, END)
    day.delete(0, END)
    assignment.delete(0, END)
    credit.delete(0, END)
    debit.delete(0, END)
    comment.delete(0, END)

######################### RIGHT SECTION ###################################


root.mainloop()