# Read and Separate Words by '#'
print("Reading A File and Separating Words by '#' ")
print("*************************************************************** ")
f = open("E:\Class 12\Computer Science\Practice.txt","r")
re = f.readlines()
for line in re :
              L = line.split(" ")
              for i in L :
                            print(i + "#",end = "")
              print()
