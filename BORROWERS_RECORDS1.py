import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="5678",database="library_management_project")
mycursor=mydb.cursor()
def borrowerstudentadd():
    Borrowers_IDp=int(input("ENTER YOUR BORROWERS_ID:- "))
    bookIDp=int(input("ENTER YOUR BOOK'S ID:- "))
    bktitlep=input("ENTER YOUR BOOK'S TITLE/NAME:- ")
    studIDp=input("ENTER YOUR STUDENT_ID:- ")
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    releaseDatep=int(input("ENTER RELEASE DATE(MMDDYYYY):- "))
    duedatep=int(input("ENTER YOUR DUE DATE(MMDDYYYY):- "))
    sql = "INSERT INTO borrowers_records (Borrowers_ID, book_ID, bktitle, stud_ID, stfname, releaseDate, dueDATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Borrowers_IDp, bookIDp, bktitlep, studIDp, stfnamep, releaseDatep, duedatep)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
def borrowerstaffadd():
    Borrowers_IDp=int(input("ENTER YOUR BORROWERS_ID:- "))
    bookIDp=int(input("ENTER YOUR BOOK'S ID:- "))
    bktitlep=input("ENTER YOUR BOOK'S TITLE/NAME:- ")
    staffIDp=input("ENTER YOUR STUDENT_ID:- ")
    stffnamep=input("ENTER YOUR FIRST NAME:- ")
    releaseDatep=int(input("ENTER RELEASE DATE(MMDDYYYY):- "))
    duedatep=int(input("ENTER YOUR DUE DATE(MMDDYYYY):- "))
    sql = "INSERT INTO borrowers_records (Borrowers_ID, book_ID, bktitle, staff_ID, stffname, releaseDate, dueDATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Borrowers_IDp, bookIDp, bktitlep, staffIDp, stffnamep, releaseDatep, duedatep)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
