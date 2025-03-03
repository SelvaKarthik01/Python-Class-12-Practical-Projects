# Lottery Program 
print("Lottery Program")
print("*************************************************************** ")
import random
print("\t$$$$$$ You Have a Chance To Win the LOTTERY !!!! $$$$$\t")
while True :
              n = int(input("Enter a Number between 1 to 6: "))
              if n in {1,2,3,4,5,6}:
                            a = 1
                            if a == n :
                                          print("$$$$$\tCongratulations!!!\t$$$$$")
                                          print("$$\tYou Won the Lottery !!!!\t$$")
                                          break
                            else :
                                          print("You Didnt Win the Lottery :( ")
                                          print("Try Again Next Time")
                                          break
              else :
                            print("Enter a Valid Number ! ")
                            
                            
