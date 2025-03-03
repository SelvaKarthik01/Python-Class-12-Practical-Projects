# All Computer Science Practical Programs in One (Program 1 - 7)
choice = 0
while choice != 3 :
              print("\t\t******All Computer Science Practical Programs in One (Program 1 - 7)********\t\t")
              print("1. Interfacing Programs 1,2 & 3 ")
              print("2. Stack Programs 5,6 & 7")
              print("3. To Exit ")
              choice = int(input("Enter Your Choice : "))
              if choice == 1 :
                            print("\t\t********Welcome to Interfacing Programs !!*********\t\t")
                            # Program No. 1,2,3 : To Create, Insert,Update,Delete & Display(Fetchall Method) Students Record using Interfacing Concepts
                            import mysql.connector as mysql
                            from prettytable import PrettyTable
                            con_obj = mysql.connect(host = "localhost",user = "root",password = "SelvaKarthik@13579@24680")
                            mycursor = con_obj.cursor()
                            def Create():
                                          Name = input("Enter the Database Name to be Created : ")
                                          L = ["Create Database {0};".format(Name),"Use {0};".format(Name)]
                                          L += ["Create table Students_Record (Roll_no int primary key, Name varchar(30),Stream varchar(20),Marks float);"]
                                          i = 0
                                          while i < len(L):
                                                        mycursor.execute(L[i])
                                                        i += 1
                                          print("Database Created Successfully !!")
                                          print()
                            def Insert():
                                          try:
                                                        n = int(input("Enter the No. of Students to be Added : "))
                                                        if n <= 0 :
                                                                      print("Invalid Entry ... Enter Number > 0 to Proceed ")
                                                                      Insert()
                                                        else :
                                                                      for i in range(n):
                                                                                    print()
                                                                                    print("Student No. ",i+1)
                                                                                    roll = int(input("Roll No. : "))
                                                                                    name = input("Name : ")
                                                                                    stream = input("Stream : ")
                                                                                    marks = float(input("Marks : "))
                                                                                    insert_stmt = "INSERT into Students_Record(Roll_No,Name,Stream,Marks) values({0},'{1}','{2}',{3});".format(roll,name,stream,marks)
                                                                                    mycursor.execute(insert_stmt)
                                                                      con_obj.commit()
                                                                      print("All Record Added Successfully !! :)")
                                          except :
                                                        con_obj.rollback()
                                                        print("Unexpected Error Occurred !")
                                                        print("Please Try Again Later |-|")
                            def Update():
                                          try:
                                                        update_roll = int(input("Enter the Roll No. to be Updated : "))
                                                        mycursor.execute("SELECT * from Students_record where Roll_no = {0};".format(update_roll))
                                                        check = mycursor.fetchone()
                                                        if check == None:
                                                                      print("Roll No. not found !! ...")
                                                                      Update()
                                                        else :
                                                                      update_marks = float(input("Enter the Marks to be Updated : "))
                                                                      update_stmt = "Update Students_Record SET Marks = {0} where Roll_No = {1};".format(update_marks,update_roll)
                                                                      mycursor.execute(update_stmt)
                                                                      con_obj.commit()
                                                                      print("Updated Successfully !! :)")
                                                                      mycursor.execute("Select * from Students_record where Roll_No = {};".format(update_roll))
                                                                      updated_record = mycursor.fetchone()
                                                                      print("Updated Record : ",updated_record)
                                          except :
                                                        con_obj.rollback()
                                                        print("Unexpected Error Occurred !")
                                                        print("Please Try Again Later |-|")
                            def Delete():
                                          try:
                                                        delete_roll = int(input("Enter the Roll No to be Deleted : "))
                                                        mycursor.execute("SELECT * from Students_Record where Roll_No = {0};".format(delete_roll))
                                                        check = mycursor.fetchone()
                                                        if check == None:
                                                                      print("Roll No. not found !! ...")
                                                                      Delete()
                                                        else :
                                                                      delete_stmt = "Delete from Students_Record where Roll_No = {};".format(delete_roll)
                                                                      mycursor.execute(delete_stmt)
                                                                      con_obj.commit()
                                                                      print("Deleted Successfully !! :)")
                                                                      print("Deleted  Record : ",check)
                                          except :
                                                        con_obj.rollback()
                                                        print("Unexpected Error Occurred !")
                                                        print("Please Try Again Later |-|")
                            def Display():
                                          mycursor.execute("SELECT * from Students_Record ;")
                                          data = mycursor.fetchall()
                                          t = PrettyTable(["Roll No","Name","Stream","Marks"])
                                          for rec in data :
                                                        t.add_row(rec)
                                          print(t)
                                          print("Total No. of Records : ",mycursor.rowcount)
                            print()
                            ch = 0
                            while ch != 6 :
                                          print("1. Create Students Record Database ")
                                          print("2. Insert Students Record " )
                                          print("3. Update Student Record ")
                                          print("4. Delete a Student Record ")
                                          print("5. Display Students Record : ")
                                          print("6. To Exit ")
                                          ch = int(input("Enter Your Choice : "))
                                          if ch == 1 :
                                                        Create()
                                          elif ch == 2 :
                                                        Insert()
                                          elif ch == 3 :
                                                        Update()
                                          elif ch == 4 :
                                                        Delete()
                                          elif ch == 5 :
                                                        Display()
                                          elif ch not in (1,2,3,4,5,6):
                                                        print("Invalid Entry ")
                            else :
                                          print("Thank You")
                            con_obj.close()
              elif choice == 2 :
                            print("\t\t******Welcome to Stack Operations !!********\t\t")
                            ch1 = 0
                            while ch1 != 4 :
                                          #Program No. 5,6 & 7 : Stack Operations - Push Pop Display using Book Details , Numbers Divisible by 5 
                                          print("1. Program 5 ")
                                          print("2. Program 6 ")
                                          print("3. Program 7 ")
                                          print("4. To Exit ")
                                          ch1 = int(input("Enter Your choice : "))
                                          if ch1 == 1 :
                                                        # Program No. 5 : Stack Operations
                                                        Stack = []
                                                        def Push(n):
                                                                      Stack.append(n)
                                                                      print("Added Sucessfully :) ")
                                                        def Pop():
                                                                      popped_value = Stack.pop()
                                                                      return popped_value
                                                        def Display():
                                                                      if len(Stack) == 0 :
                                                                                    print("Stack is Empty ^_^")
                                                                      else :
                                                                                    print(Stack[-1]," <----- Top |>")
                                                                                    for i in range(len(Stack)-2,-1,-1):
                                                                                                  print(Stack[i])
                                                                                    print()
                                                        ch = 0
                                                        while ch != 4 :
                                                                      print("1. Push")
                                                                      print("2. Pop")
                                                                      print("3. Display")
                                                                      print("4. To Exit ")
                                                                      ch =int(input("Enter Your Choice : "))
                                                                      if ch == 1 :
                                                                                    n = int(input("Enter the number to be Pushed : "))
                                                                                    Push(n)
                                                                      elif ch == 2 :
                                                                                    if len(Stack) == 0 :
                                                                                                  print("UnderFlowing Error !!")
                                                                                                  print("Stack is Empty !!")
                                                                                    else :
                                                                                                  result = Pop()
                                                                                                  print("Popped_Value : ",result)
                                                                      elif ch == 3 :
                                                                                    Display()
                                                                      elif ch not in (1,2,3,4):
                                                                                    print("Invalid Entry !")
                                                        else :
                                                                      print("Thank You !!")

                                          elif ch1 == 2 :
                                                        # Program No. 6 : Push, Pop and Display Book Details Using Stack Operations
                                                        Stack = []
                                                        def Push(Book_details):
                                                                      Stack.append(Book_details)
                                                                      print("Added Successfully ! :)")
                                                        def Pop():
                                                                      if len(Stack) == 0 :
                                                                                    print("Underflowing Error !!")
                                                                                    print("Stack is Empty ^-^")
                                                                      else :
                                                                                    Popped_value = Stack.pop()
                                                                                    return Popped_value
                                                        def Display():
                                                                      if len(Stack) == 0 :
                                                                                    print("Stack is Empty ^-^")
                                                                      else :
                                                                                    print(Stack[-1]," <---- Top |>")
                                                                                    for i in range(len(Stack)-2,-1,-1):
                                                                                                  print(Stack[i])
                                                                                    print()
                                                        ch = 0
                                                        while ch != 4 :
                                                                      print("1. Push Book Details")
                                                                      print("2. Pop Book Details ")
                                                                      print("3. Display Book Details ")
                                                                      print("4. To Exit : ")
                                                                      ch = int(input("Enter Your Choice : "))
                                                                      if ch == 1 :
                                                                                    book_no = int(input("Enter Book No. "))
                                                                                    book_name = input("Enter Book Name : ")
                                                                                    book_details = [book_no,book_name]
                                                                                    Push(book_details)
                                                                      elif ch == 2 :
                                                                                    result = Pop()
                                                                                    print("Popped Value : ",result)
                                                                      elif ch == 3:
                                                                                    Display()
                                                                      elif ch not in (1,2,3,4):
                                                                                    print("Invalid Entry ")
                                                        else :
                                                                      print("Thank You")
                                          elif ch1 == 3 :
                                                        #Program No. 7 : Push, Pop and Display only those Numbers Divisible by 5 using Stack Operations
                                                        Stack = []
                                                        def Push(List):
                                                                      for i in List :
                                                                                    Stack.append(i)
                                                                      print("Added Successfully !! :)")
                                                        def Pop():
                                                                      Popped_value = Stack.pop()
                                                                      return Popped_value
                                                        def Display():
                                                                      if len(Stack) == 0 :
                                                                                    print("Stack is Empty ^-^")
                                                                      else :
                                                                                    print(Stack[-1]," <----- Top |>")
                                                                                    for i in range(len(Stack)-2,-1,-1):
                                                                                                  print(Stack[i])
                                                                                    print()
                                                        ch = 0
                                                        while ch != 4 :
                                                                      print("1. Push ")
                                                                      print("2. Pop ")
                                                                      print("3. Display ")
                                                                      print("4. To Exit ")
                                                                      ch = int(input("Enter Your Choice : "))
                                                                      if ch == 1 :
                                                                                    L = eval(input("Enter the List of Numbers to be Added : "))
                                                                                    List = []
                                                                                    thrown_values = []
                                                                                    for i in L :
                                                                                                  if i % 5 == 0 :
                                                                                                                List += [i]
                                                                                                                
                                                                                                  else :
                                                                                                                thrown_values += [i]

                                                                                    Push(List)
                                                                                    print("List of Values not Appended : ",thrown_values)
                                                                      elif ch == 2 :
                                                                                    if len(Stack) == 0 :
                                                                                                  print("Underflowing Error !!")
                                                                                                  print("Stack is Empty ^-^")
                                                                                    else :
                                                                                                  result = Pop()
                                                                                                  print("Popped Value : ",result)
                                                                      elif ch == 3 :
                                                                                    Display()
                                                                      elif ch not in (1,2,3,4):
                                                                                    print("Invalid Entry ")
                                                        else :
                                                                      print("Thank You")
                                          elif ch1 not in (1,2,3,4):
                                                        print("Invalid Entry ")
                            else :
                                          print("Thank You")
              elif choice not in (1,2,3):
                            print("Invalid Entry")
else :
              print("Thank You U_U")
                            
                                                                                    
                                                                                                  
                                                        
                                          
                                          
                                                        
