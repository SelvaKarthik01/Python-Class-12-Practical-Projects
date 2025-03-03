# Progam No. 1 : Interface - Create, Insert and Display (Fetchall method) Using Students Record
print()
import mysql.connector as mysql
from prettytable import PrettyTable
con_obj = mysql.connect(host = "localhost",user = 'root',password = "SelvaKarthik@13579@24680")
mycursor = con_obj.cursor()
L = ["Create Database School;","Use School;"]
L +=["Create Table Students_Record(Roll_No int Primary key,Name varchar(50),Stream varchar(20),Marks float);"]
i = 0
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
              con_obj.commit()
              print("Added Successfully!")
except :
              con_obj.rollback()
              print("Unexpected Error Occurred !")
              print("Please Try Again")

ch = input("Do you Want to Display the Student Records (Y/N) : ")
if ch == "Y" or ch == "y" :
              mycursor.execute("Select * from Students_Record;")
              data = mycursor.fetchall()
              print(type(data))
              t = PrettyTable(["Roll No.","Name","Stream","Marks"],padding_width=5)
              for rec in data :
                            t.add_row(rec)
              print(t)
              row_count = mycursor.rowcount
else :
              print("Thank You")
con_obj.close()
              

              




              
