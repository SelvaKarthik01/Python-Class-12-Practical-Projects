# Fibonocci Series for N numbers
print("Fibonocci Series")
print("*************************************************************** ")
n = int(input("Enter N to Print Fibonocci Series : "))
if n > 0 :
              count = 0
              a = 0
              b = 1
              print(0,1,end = " ")
              n -= 2
              while count < n :
                            c = a + b
                            print(c,end = " ")
                            a = b
                            b = c
                            count += 1
else :
              print("Enter a +ve Value for N !!")

