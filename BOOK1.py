import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="5678",database="library_management_project")
mycursor=mydb.cursor()
def bookadd():
    bookIDp=input("ENTER THE BOOK'S ID:- ") 
    bktitlep=input("ENTER THE BOOK'S TITLE/NAME:- ")
    bkauthorp=input("ENTER THE BOOK'S AUTHOR NAME:- ")
    bkpublisherp=input("ENTER THE BOOK'S PUBLISHER NAME:- ")
    bkcopiesp=int(input("ENTER THE TOTAL NUMBER OF THE COPIES OF THIS BOOK:- "))
    bk_sourcep=input("ENTER THE BOOK'S SOURCE:- ")
    bk_costp=int(input("ENTER THE BOOK'S COST OF ONE UNIT:- "))
    bk_remarksp=input("ENTER BOOK'S REMARKS:- ")
    sql = "INSERT INTO BOOK (book_ID, bktitle, bkedition, bkauthor, bkpublisher, bkcopies, bk_source, bk_cost, bk_remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (bookIDp, bktitlep, bkauthorp, bkpublisherp, bkcopiesp, bk_sourcep, bk_costp, bk_remarksp)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
def bookupdate(bookID):
    bookIDp=input("ENTER THE BOOK'S ID:- ")
    bktitlep=input("ENTER THE BOOK'S TITLE/NAME:- ")
    bkauthorp=input("ENTER THE BOOK'S AUTHOR NAME:- ")
    bkpublisherp=input("ENTER THE BOOK'S PUBLISHER NAME:- ")
    bkcopiesp=int(input("ENTER THE TOTAL NUMBER OF THE COPIES OF THIS BOOK:- "))
    bk_sourcep=input("ENTER THE BOOK'S SOURCE:- ")
    bk_costp=int(input("ENTER THE BOOK'S COST OF ONE UNIT:- "))
    bk_remarksp=input("ENTER BOOK'S REMARKS:- ")
    sql = "UPDATE BOOK SET book_ID = %s, bktitle = %s, bkedition = %s, bkauthor = %s, bkpublisher = %s, bkcopies = %s, bk_source = %s, bk_cost = %s, bk_remarks = %s WHERE book_ID = bookID"
    val = (bookIDp, bktitlep, bkauthorp, bkpublisherp, bkcopiesp, bk_sourcep, bk_costp, bk_remarksp)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "records updated")
