import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk



from Login import *
import tkinter.messagebox as mb
def RegisterWindow():

    root.geometry("600x600")
    root.title("Add Student  Record Page")
    C = Canvas(root, bg="blue", height=500, width=500)

    # Definging the first row
    lblstudentid = tk.Label(root, text="STUDENTID -", )
    lblstudentid.place(x=50, y=20)

    root.STUDENTID = tk.Entry(root, width=35)
    root.STUDENTID.place(x=150, y=20, width=100)

    root.lblname = tk.Label(root, text="Name -", )
    root.lblname.place(x=50, y=50)

    root.NAME = tk.Entry(root, width=35)
    root.NAME.place(x=150, y=50, width=100)

    lblclass = tk.Label(root, text="CLASS -")
    lblclass.place(x=50, y=100)

    root.CLASS = tk.Entry(root, width=35)
    root.CLASS.place(x=150, y=100, width=100)

    lbladdress = tk.Label(root, text="ADDRESS -", )
    lbladdress.place(x=50, y=150)

    root.ADDRESS = tk.Entry(root, width=35)
    root.ADDRESS.place(x=150, y=150, width=100)

    lblcontactno = tk.Label(root, text="ContactNO-")
    lblcontactno.place(x=50, y=200)

    root.CONTACTNO = tk.Entry(root, width=35)
    root.CONTACTNO.place(x=150, y=200, width=100)

    lblschool = tk.Label(root, text="SCHOOL-")
    lblschool.place(x=50, y=250)

    root.SCHOOL = tk.Entry(root, width=35)
    root.SCHOOL.place(x=150, y=250, width=100)

    lbldateofjoining = tk.Label(root, text="DATE OF JOINING -", )
    lbldateofjoining.place(x=50, y=300)

    root.DATEOFJOINING = tk.Entry(root, width=35)
    root.DATEOFJOINING.place(x=150, y=300, width=100)

    lblclassperhour = tk.Label(root, text="CLASSPERHOUR -")
    lblclassperhour.place(x=50, y=350)

    root.CLASSPERHOUR = tk.Entry(root, width=35)
    root.CLASSPERHOUR.place(x=150, y=350, width=100)

    lblmonthlypay = tk.Label(root, text="MONTHLYPAY -", )
    lblmonthlypay.place(x=50, y=400)

    root.MONTHLYPAY = tk.Entry(root, width=35)
    root.MONTHLYPAY.place(x=150, y=400, width=100)

    lbllumpsumpayment = tk.Label(root, text="LUMPSUMPAYMENT -")
    lbllumpsumpayment.place(x=50, y=450)

    root.LUMPSUMPAYMENT = tk.Entry(root, width=35)
    root.LUMPSUMPAYMENT.place(x=150, y=450, width=100)

    lblenrollsubject1 = tk.Label(root, text="ENROLLSUBJECT1 -")
    lblenrollsubject1.place(x=50, y=500)

    root.ENROLLSUBJECT1 = tk.Entry(root, width=35)
    root.ENROLLSUBJECT1.place(x=150, y=500, width=100)

    lblenrollsubject2 = tk.Label(root, text="ENROLLSUBJECT2-", )
    lblenrollsubject2.place(x=50, y=550)

    root.ENROLLSUBJECT2 = tk.Entry(root, width=35)
    root.ENROLLSUBJECT2.place(x=150, y=550, width=100)

    lblenrollsubject3 = tk.Label(root, text="ENROLLSUBJECT3 -")
    lblenrollsubject3.place(x=50, y=600)

    root.ENROLLSUBJECT3 = tk.Entry(root, width=35)
    root.ENROLLSUBJECT3.place(x=150, y=600, width=100)

    submitbtn = tk.Button(root, text="Register",
                          bg='blue', command=addstudentrecord)
    submitbtn.place(x=150, y=650, width=55)



def addstudentrecord():

    studentid = root.STUDENTID.get()
    name =root. NAME.get()
    stclass = root.CLASS.get()
    address = root.ADDRESS.get()
    mn = root.CONTACTNO.get()
    school = root.SCHOOL.get()
    dateofjoining = root.DATEOFJOINING.get()
    classperhour = root.CLASSPERHOUR.get()
    monthly = root.MONTHLYPAY.get()
    lumpsumamount = root.LUMPSUMPAYMENT.get()
    enrollsubject1 = root.ENROLLSUBJECT1.get()
    enrollsubject2 = root.ENROLLSUBJECT2.get()
    enrollsubject3 = root.ENROLLSUBJECT3.get()

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql")
        mycursor = mydb.cursor()
        mycursor.execute("create database if not exists mayankinstitute")
        mycursor.execute("use mayankinstitute")
        mycursor.execute(
            "create table if not exists strecord(studentid varchar(10) unique,name varchar(100) primary key,stclass varchar(50),address char(150), mobileno char(10),school varchar(50),dateofjoining date ,classperhour varchar(50) null,monthly varchar(50) null,lumpsumamount varchar(50),enrollsubject1 varchar(30),enrollsubject2 varchar(30) null,enrollsubject3 varchar(30) null)")

        query = mycursor.execute(
            "insert into strecord values('" + studentid + "','" + name + "','" + stclass + " ','" + address + "','" + mn + "','" + school + "','" + dateofjoining + "','" + classperhour + "','" + monthly + "','" + lumpsumamount + "','" + enrollsubject1 + " ','" + enrollsubject2 + "','" + enrollsubject3 + "')")
        mydb.commit()
        print(query)  # implement sql Sentence
        mycursor.execute(query)
        mb.showinfo('Information', "Data inserted Successfully")
        mydb.commit()
        print("Student Record is successfully created!!!")
    except:
        mydb.rollback()
        print("Error occured")
        mydb.close()
        onClose()

def onClose():
        """"""
        root.destroy()
        root.original_frame.show()
def attendanceofstudent ():
        import attendance


def searchattendance():
    import searchrecord



def main():
        root.title('Open New Window!!!')
        root.geometry("400x400")
        #root.resizable(0, 0)
        a1 = ttk.Button(root, text="ADD Student Record", command=RegisterWindow).grid(row=0, column=0)
        b1 = ttk.Button(root, text="Attendance Of Student", command=attendanceofstudent).grid(row=1, column=0)
        c1 = ttk.Button(root, text=" Search Attendance", command=searchattendance).grid(row=2, column=0)


root=Tk()
main()
root.mainloop()
