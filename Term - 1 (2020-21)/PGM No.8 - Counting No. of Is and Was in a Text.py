# Read and Count Occurence of 'is' and 'was'
print("Reading a File and Counting No. of Occurence of 'is' and 'was' ")
print("*************************************************************** ")
print()
f = open("E:\Class 12\Computer Science\Practice.txt","r")
re = f.read()
cis ,cwas = 0,0
L = re.split(" ")
for i in L :
              i = i.lower()
              if i == "is" :
                            cis += 1
              elif i == "was" :
                            cwas += 1
print("No. of Occurence of Word 'is' : ",cis)
print("No. of Occurence of Word 'was' : ",cwas)
