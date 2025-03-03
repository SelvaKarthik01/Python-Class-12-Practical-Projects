# Create, Read and Update an Binary File
print("Updating a Record in a Binary File")
print("*************************************************************** ")
import pickle
def create() :
              f = open("E:\Class 12\Computer Science\File_Binary.dat","wb")
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
              f = open("E:\Class 12\Computer Science\File_Binary.dat","rb")
              print()
              print("Roll No. ","\t","\tName\t","\t","Average")
              while True :
                            try :
                                          content = pickle.load(f)
                                          print(content[0],end = "\t\t")
                                          print(content[1],end = "\t\t")
                                          print(content[2])
                            except EOFError :
                                          break
              print()          
              f.close()
def Update() :
              f = open("E:\Class 12\Computer Science\File_Binary.dat","rb+")
              update = int(input("Enter the Roll No. to be Updated : "))
              while True :
                            try :
                                          pos = f.tell()
                                          content = pickle.load(f)
                                          if update == content[0]:
                                                        update_avg = float(input("Enter the Average To be Updated : "))
                                                        content[2] = update_avg
                                                        f.seek(pos)
                                                        pickle.dump(content,f)
                                                        print("Successfully Updated !!")
                                                        print("Roll No : ",content[0])
                                                        print("Name : ",content[1])
                                                        print("Average : ",content[2])
                                                        break
                            except EOFError :
                                          print("Roll No not found in File !!")
                                          break
              f.close()                                      
ch = 0
while ch != 4 :
              print("1. Create Binary File ")
              print("2. Read Binary File ")
              print("3. Update Binary File ")
              print("4. Exit ")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            create()
              elif ch == 2 :
                            read()
              elif ch == 3 :
                            Update()
else :
              print("Thank You")

              
