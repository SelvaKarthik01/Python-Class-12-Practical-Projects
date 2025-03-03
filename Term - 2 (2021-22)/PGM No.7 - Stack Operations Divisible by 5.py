# Program No. 7 - Stack Operations Push (Divisible by 5), Pop and Display
stack = []
def Push(List):
              for i in List :
                            if i % 5 == 0 :
                                          stack.append(i)
              print("Done |>")
def Pop():
              pop_value = stack.pop()
              print("Popped Value : ",pop_value)
def Display() :
              print()
              print(stack[-1],"<--- top")
              for i in range(len(stack)-2,-1,-1):
                            print(stack[i])
              print()
ch = 0
while ch != 4 :
              print("1. Push")
              print("2. Pop")
              print("3. Display")
              print("4. To Exit")
              ch = int(input("Enter Your Choice : "))
              if ch == 1 :
                            L = eval(input("Enter the List of Numbers : "))
                            Push(L)
              elif ch == 2 :
                            Pop()
              elif ch == 3 :
                            Display()
else :
              print("Thank You")
              
                            
              
