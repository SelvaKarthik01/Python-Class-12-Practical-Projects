# Create and Read an Binary File 
print("Creating and Reading Student Record in a Binary File")
print("*************************************************************** ")
import pickle
def create() :
              f = open(r"E:\Class 12\Computer Science\File_Binary.dat","ab")
              n = int(input("Enter the No. of Students to be Added : "))
              for i in range(n):
                            print("Student No. ",i+1)
                            name = input("Name : ")
                            roll = int(input("Roll No : "))
                            avg = float(input("Average Marks : "))
                            pickle.dump([roll,name,avg],f)
              print("Added Successfully !!")
              f.close()
def read():
              f = open(r"E:\Class 12\Computer Science\File_Binary.dat","rb")
              print()
              print("Roll No. ","\t","\tName\t","\t","Average")
              while True :
                            try :
                                          content = pickle.load(f)
                                          print(content)
                                          print(content[0],end = "\t\t")
                                          print(content[1],end = "\t\t")
                                          print(content[2])
                            except EOFError :
                                          break
              print()          
              f.close()
ch = 0
while ch != 3 :
              print("1. Create Binary File ")
              print("2. Read the Binary File ")
              print("3. Exit ")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            create()
              elif ch == 2 :
                            read()
else :
              print("Thank You ")
              

              
