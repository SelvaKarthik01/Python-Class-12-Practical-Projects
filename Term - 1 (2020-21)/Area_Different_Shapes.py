#Imported Module in Main Program
def Rectangle() :
              l = int(input("Enter the Length (in cm) :"))
              b = int(input("Enter the Breadth (in cm) :"))
              area = l*b
              perimeter = 2 *(l+b)
              print("Area of Rectangle : ",area,"sq.cm")
              print("Perimeter of Rectangle : ",perimeter,"cm")
def Square():
              a = int(input("Enter the Length of Side of Square (in cm): "))
              area = a*a
              perimeter = 4*a
              print("Area of Square : ",area,"sq.cm")
              print("Perimeter of Square : ",perimeter,"cm")
def Circle():
              r = int(input("Enter the Radius Of Circle (in cm) : "))
              area = 3.14 *r*r
              perimeter = 2*3.14*r
              print("Area of Circle : ",area,"sq.cm")
              print("Circumference of Circle : ",perimeter,"cm")

