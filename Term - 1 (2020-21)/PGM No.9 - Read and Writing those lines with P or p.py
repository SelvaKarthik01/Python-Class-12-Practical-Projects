# Reading and Writing Those lines Starting with 'P'
print("Reading a File and Writing those Lines that Starts with Letter 'P' in Another File")
print("*************************************************************************************************** ")
fin = open("E:\Class 12\Computer Science\Practice.txt","r")
fout = open("E:\Class 12\Computer Science\Write.txt","w+")
while True:
              try:
                  line = fin.readline()
                  if line[0] == 'p' or 'P':
                                fout.write(line)
              except IndexError :
                            break
print('Successfully Copied the lines starting with P character')
n = input(r"Do You Want View the Contents Inside the File (Y\N) : ")
if n == "y" or n == "Y" :
              fout.seek(0)
              print(fout.read())
else :
              print("Thank You")
fin.close()
fout.close()
            
                            
                            
                            
