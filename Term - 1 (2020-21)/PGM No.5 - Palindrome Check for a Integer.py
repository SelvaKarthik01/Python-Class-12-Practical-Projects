# Palindrome Check for an Integer
print("Palindrome Check for an Interger ")
print("*************************************************************** ")
n = int(input("Enter the No. to be Checked : "))
if n < 0 :
              print("Palindrome Cannot be Checked for a Negative Number ")
elif n > 0 and n < 10 :
              print("Palindrome Cannot be Checked for a Single Digit Number ")
else :
              t = n
              s = 0
              while t!= 0 :
                            a = t % 10
                            s = s * 10
                            s = s + a
                            t = t // 10
              if n == s :
                            print(n , "Is a Palindrome ! ")
              else :
                            print(n, "Is not a Palindrome ! ")
