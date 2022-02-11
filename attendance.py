import tkinter as tk
import mysql.connector
from tkinter import *

import tkinter.messagebox as mb
from Features import *
def attendanceofstudent ():

    root.geometry("600x600")
    root.title("Add Student  Record Page")
    C = Canvas(root, bg="blue", height=500, width=500)

    # Definging the first row
    lblname1 = tk.Label(root, text="Name -", )
    lblname1.place(x=50, y=20)

    root.name1 = tk.Entry(root, width=35)
    root.name1.place(x=150, y=20, width=100)

    root.lbldateofclass1 = tk.Label(root, text="Date Of Class-", )
    root.lbldateofclass1.place(x=50, y=50)

    root.dateofclass1 = tk.Entry(root, width=35)
    root.dateofclass1.place(x=150, y=50, width=100)

    lbldiscussionstartingtime1 = tk.Label(root, text="Discussion Staring Time -")
    lbldiscussionstartingtime1.place(x=50, y=100)

    root.discussionstartingtime1 = tk.Entry(root, width=35)
    root.discussionstartingtime1.place(x=150, y=100, width=100)

    lblsubject1 = tk.Label(root, text="Subject-", )
    lblsubject1.place(x=50, y=150)

    root.subject1 = tk.Entry(root, width=35)
    root.subject1.place(x=150, y=150, width=100)

    lblstclasshr1= tk.Label(root, text=" Class Hour-")
    lblstclasshr1.place(x=50, y=200)

    root.stclasshr1 = tk.Entry(root, width=35)
    root.stclasshr1.place(x=150, y=200, width=100)

    lbltopicdiscussion1 = tk.Label(root, text=" Topic Discussion-")
    lbltopicdiscussion1.place(x=50, y=250)

    root.topicdiscussion1 = tk.Entry(root, width=35)
    root.topicdiscussion1.place(x=150, y=250, width=100)
    submitbtn = tk.Button(root, text="Submit",
                          bg='blue', command=onlineattendance)
    submitbtn.place(x=150, y=300, width=55)
def onlineattendance():
    name = root.name1.get()
    dateofclass = root.dateofclass1.get()
    discussiontime = root.discussionstartingtime1.get()
    subject = root.subject1.get()
    stclasshr = root.stclasshr1.get()
    topicdiscussion = root.topicdiscussion1.get()
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists mayankinstitute")
        mycursor.execute("use mayankinstitute")
        mycursor.execute(
            "create table if not exists attendance(name varchar(50),dateofclass date ,discussiontime varchar(50),subject varchar(30),stclasshr varchar(30),topicdiscussion varchar(30),foreign key (name) references strecord(name))")
        #mycursor.execute("select * from strecord where name='" + name + "'")
        mycursor.execute(
            "insert into attendance values('" + name + "','" + dateofclass + "','" + discussiontime + "','" + subject + "','" + stclasshr + " ','" + topicdiscussion + "')")
        mydb.commit()
        print("Student Record is successfully created!!!")


        mb.showinfo('Information', "Data inserted Successfully")
        mydb.commit()
        print("Student Record is successfully created!!!")
    except:
        mydb.rollback()
        mb.showinfo('Information', "Data Insertion Failed")
        print("Error occured")
        mydb.close()

root=tk.Tk()
attendanceofstudent   ()
root.mainloop()