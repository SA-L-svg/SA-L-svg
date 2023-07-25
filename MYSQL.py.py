from tabulate import tabulate
import mysql.connector


con = mysql.connector.connect(host='localhost', user='root', password="Auto@1224", database="python_db")


def select():
    res = con.cursor()
    sql = "select STUDENTID,NAM,AGE,CITY,MARKS from studentss"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=['STUDENTID', 'NAM', 'AGE', 'CITY', 'MARKS']))


def insert(nam, age, city, marks):
    res = con.cursor()
    sql = "insert into studentss (nam, age, city, marks) values (%s,%s,%s,%s)"
    student = (nam, age, city, marks)
    res.execute(sql, student)
    con.commit()
    print("Data Insert success")


def update(nam, age, city, marks, id):
    res = con.cursor()
    sql = "update studentss set NAM=%s,AGE=%s,CITY=%s,MARKS=%s where studentid=%s"
    student = (nam, age, city, marks, id,)
    res.execute(sql, student,)
    con.commit()
    print("Data Update success")


def delete(STUDENTID):
    res = con.cursor()
    sql = "delete from studentss  where STUDENTID=%s"
    student = (STUDENTID,)
    res.execute(sql, student,)
    con.commit()
    print("Data DELETE success")


while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit Data")

    choice = int(input("Enter the choice: "))


    if choice == 1:

        nam  = input("Enter the name: ")
        age = input("Enter the age: ")
        city = input("Enter the city: ")
        marks = input("Enter the marks: ")
        insert(nam, age, city, marks)



    elif choice == 2:
        id = input("Enter the ID: ")
        NAM = input("Enter the name: ")
        AGE = input("Enter the age: ")
        CITY = input("Enter the city: ")
        marks = input("Enter the marks: ")

        update(NAM, AGE, CITY, marks, id)
    elif choice == 3:
        select()

    elif choice == 4:
        STUDENTID = input("Enter the Id  to Delete : ")
        delete(STUDENTID)
    elif choice == 5:
        quit()
    else:
        print("Invaild selection .please try again")
