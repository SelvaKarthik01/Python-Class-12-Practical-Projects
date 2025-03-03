# Finding Factorial of a Number
print("Factorial of a Number")
print("*************************************************************** ")
n = int(input("Enter a Number to find the Factorial of it : "))
if n < 0 :
              print("Factorial for a Negative Number is Not Possible !! ")
else :
              p = 1
              for i in range(n,0,-1):
                            p *= i
              print(n," ! = ",p)
