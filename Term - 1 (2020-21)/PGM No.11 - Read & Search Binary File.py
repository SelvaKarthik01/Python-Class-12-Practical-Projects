# Creating and Searching an Binary File 
print("Creating & Searching a Record in a Binary File")
print("*************************************************************** ")
import pickle
def create() :
              f = open("E:\Class 12\Computer Science\File_Binary.dat","ab")
              n = int(input("Enter the No. of Students to be Added : "))
              for i in range(n):
                            print("Student No. ",i+1)
                            name = input("Name : ")
                            roll = int(input("Roll No : "))
                            avg = float(input("Average Marks : "))
                            pickle.dump([roll,name,avg],f)
              print("Added Successfully !!")
              f.close()
def search():
              f = open("E:\Class 12\Computer Science\File_Binary.dat","rb")
              search = int(input("Enter the Roll No. of to be Searched : "))
              while True :
                            try :
                                          content = pickle.load(f)
                                          if content[0] == search :
                                                        print("Roll No : ",content[0])
                                                        print("Name : ",content[1])
                                                        print("Average : ",content[2])
                                                        break
                            except EOFError :
                                          print("Roll No. Not Found in File !!! ")
                                          break
              f.close()
ch = 0
while ch != 3 :
              print("1. Create Binary File ")
              print("2. Search Binary File ")
              print("3. Exit ")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            create()
              elif ch == 2 :
                            search()
else :
              print("Thank You")
