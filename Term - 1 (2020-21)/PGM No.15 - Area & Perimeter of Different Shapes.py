# Calculate Area and Perimeter of Different Shapes
print("Finding Area & Perimeter of Different Shapes")
print("*************************************************************** ")
import Area_Different_Shapes as a # Importing Previously Created Module
ch = 0
while ch != 4 :
              print("1. Area & Perimeter of Rectangle ")
              print("2. Area & Perimeter of Square ")
              print("3. Area & Perimeter of Circle ")
              print("4. Exit ")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            a.Rectangle()
              elif ch == 2 :
                            a.Square()
              elif ch == 3 :
                            a.Circle()
else :
              print("Thank You")
