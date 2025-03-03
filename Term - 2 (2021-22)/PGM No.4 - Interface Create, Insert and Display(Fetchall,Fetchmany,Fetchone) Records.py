# Progam No. 4 : Interface - Create, Insert and Display(FetchAll,Fetchone,Fetchmany) using Students Record
import mysql.connector as mysql
from prettytable import PrettyTable
con_obj = mysql.connect(host = "localhost",user = 'root',password = "SelvaKarthik@13579@24680")
mycursor = con_obj.cursor()
L = ["Create Database School;","Use School;"]
L += ["Create Table Students_Record(Roll_No int Primary key,Name varchar(50),Stream varchar(20),Marks float);"]
i = 0
def fetchall():
              con_obj = mysql.connect(host = "localhost",user = 'root',password = "SelvaKarthik@13579@24680",database = "School")
              mycursor = con_obj.cursor()
              print("Fetchall Method")
              print()
              mycursor.execute("Select * from Students_Record;")
              data = mycursor.fetchall()
              t = PrettyTable(["Roll No.","Name","Stream","Marks"],padding_width=5)
              for rec in data :
                            t.add_row(rec)
              print(t)
              row_count = mycursor.rowcount
              print("Total No. of Records : ",row_count)
              con_obj.close()
def fetchmany():
              con_obj = mysql.connect(host = "localhost",user = 'root',password = "SelvaKarthik@13579@24680",database = "School")
              mycursor = con_obj.cursor()
              print("Fetchmany Method")
              print()
              mycursor.execute("Select * from Students_Record;")
              n = int(input("Enter the No. of Records to be Displayed : "))
              data = mycursor.fetchmany(n)
              t = PrettyTable(["Roll No.","Name","Stream","Marks"])
              for rec in data :
                             t.add_row(rec)
              print(t)
              row_count = mycursor.rowcount
              print("Total No. of Records : ",row_count)
              con_obj.close()
def fetchone():
              con_obj = mysql.connect(host = "localhost",user = 'root',password = "SelvaKarthik@13579@24680",database = "School")
              mycursor = con_obj.cursor()
              print("Fetchone Method")
              print()
              n = int(input("Enter the No. of Records to be Displayed : "))
              mycursor.execute("Select * from Students_Record;")
              t = PrettyTable(["Roll No.","Name","Stream","Marks"])
              for i in range(n):
                            data = mycursor.fetchone()
                            t.add_row(data)
              print(t)
              row_count = mycursor.rowcount
              print("Total No. of Records : ",row_count)
              con_obj.close()    
              
while i < len(L):
              mycursor.execute(L[i])
              i += 1
try :
              n = int(input("Enter the Number of Students to be Added : "))
              for i in range(n):
                            print()
                            print("Student No. ",i+1)
                            Roll = int(input("Roll No. :"))
                            Name = input("Name : ")
                            Stream = input("Stream : ")
                            Marks = float(input("Marks : "))
                            insert_stm = "Insert into Students_Record(Roll_No,Name,Stream,Marks) values ({0},'{1}','{2}',{3})".format(Roll,Name,Stream,Marks)
                            mycursor.execute(insert_stm)
              count = mycursor.rowcount
              con_obj.commit()
              print("Added Successfully!")
except :
              con_obj.rollback()
              print("Unexpected Error Occurred !")
              print("Please Try Again")

ch = 0
while ch != 4 :
              print("1. Display Using Fetchall Method")
              print("2. Display Using Fetchmany Method")
              print("3. Display Using Fetchone Method")
              print("4. To Exit")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            fetchall()
                            
              elif ch == 2 :
                            fetchmany()
                            
              elif ch == 3 :
                            fetchone()
                            
else :
              print("Thank You")
con_obj.close()
                                          
                                          
                            




                            
