# Reading And Counting Vowels, Consonents, Uppcase and Lowercases
print("Reading A File and Counting the No. of Vowels, Consonents,Uppercase and Lowercase Alphabets")
print("********************************************************************************************************************")
f = open("E:\Class 12\Computer Science\Practice.txt","r")
re = f.read()
v,con,u,l = 0,0,0,0
for i in re :
              if i .isalpha():
                            if i in "AEIOUaeiou":
                                          v += 1
                            elif i not in "AEIOUaeiou":
                                          con += 1
                            if i.isupper() :
                                          u += 1
                            elif i.islower():
                                          l += 1
print("No. of Vowels In Text : ",v)
print("No. of Consonents In Text : ",con)
print("No. of Upper Case Alphabets In Text : ",u)
print("No. of Lower Case Alphabets In Text : ",l)
f.close()
