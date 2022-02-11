import tkinter as tk
import mysql.connector
from tkinter import *

import tkinter.messagebox as mb

from Features import *
def searchattendance():
    #root=tk.TK()
    root.geometry("600x600")
    root.title("Searching  Page")
    C = Canvas(root, bg="blue", height=500, width=500)

    # Definging the first row
    lblname = tk.Label(root, text="Name -", )
    lblname.place(x=50, y=20)

    root.name = tk.Entry(root, width=35)
    root.name.place(x=150, y=20, width=100)

    submitbtn = tk.Button(root, text="Submit",
                          bg='blue', command=search)
    submitbtn.place(x=150, y=50, width=55)

def search():
    #root=tk.Tk()
    name1 = root.name.get()
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists mayankinstitute")
        mycursor.execute("use mayankinstitute")
        mycursor.execute("select * from attendance where name='" + name1 + "'")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        #print(query)  # implement sql Sentence
        #mycursor.execute(query)
        #mb.showinfo('Information', "Data inserted Successfully")
        mydb.commit()
        print("Student Record is successfully displayed!!!")
    except:
        mydb.rollback()
        print("Error occured")
        mydb.close()
root=tk.Tk()
searchattendance()
root.mainloop()