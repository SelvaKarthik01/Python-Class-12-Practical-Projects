# Program 5 : Stack Operations - Push, Pop and Display

stack = []
def push(n):
              stack.append(n)
def pop():
               pop_value = stack.pop()
               return pop_value
def display():
              print(stack[-1]," <---- TOP")
              for i in range(len(stack)-2,-1,-1):
                            print(stack[i])

ch = 0
while ch != 4 :
              print("1. Push")
              print("2. Pop")
              print("3. Display")
              print("4.To Exit ")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            n = int(input("Enter the Value to be Pushed into the Stack : "))
                            push(n)
              elif ch == 2 :
                            if len(stack) == 0 :
                                          print("Stack is Empty !")
                            else :
                                          result = pop()
                                          print("Popped Value : ",result)
              elif ch == 3 :
                            display()
else :
              print("Thank You")
