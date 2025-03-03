# Create and Read a CSV File 
print("Creating & Searching an Employee Record in a CSV File ")
print("******************************************************************** ")
import csv
def Create():
              f = open("E:\Class 12\Computer Science\Employee_Details.csv","a",newline= '')
              file_writer = csv.writer(f)
              print(file_writer)
              n = int(input("Enter the No. of Employees to be Added : "))
              for i in range(n):
                            print("Employee No. ",i+1)
                            print()
                            Emp_No = int(input("Employee ID : "))
                            Name = input("Name : ")
                            sal = float(input("Salary : "))
                            print()
                            file_writer.writerow([Emp_No,Name,sal])
              print("Added Successfully !! ")
              f.close()
def Search():
              f = open("E:\Class 12\Computer Science\Employee_Details.csv","r")
              search = input("Enter the Employee ID to be Searched : ")
              reader = csv.reader(f)
              print(reader)
              print()
              for i in reader :
                            if i[0] == search :
                                          print("Employee ID : ",i[0])
                                          print("Name : ",i[1])
                                          print("Salary : " ,i[2])
                                          print()
                                          break
              else :
                            print("Employee ID Not Found !!!")
              f.close()

ch = 0
while ch != 3 :
              print("1.Add Employee Details ")
              print("2. Search An Employee ")
              print("3. To Exit ")
              ch = int(input("Enter the Your Choice : "))
              if ch == 1 :
                            Create()
              elif ch == 2 :
                            Search()
else :
              print("Thank You")
