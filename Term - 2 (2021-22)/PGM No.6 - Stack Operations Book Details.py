# Program 6 : Stack Opertaions : Push, Pop and Display Book Details
stack_books = []
def Push(list_pushed):
              stack_books.append(list_pushed)
              print("Done |>")
def Pop():
              pop_value = stack_books.pop()
              return pop_value
def Display():
              print()
              print(stack_books[-1],"<---- top")
              for i in range(len(stack_books)-2,-1,-1):
                            print(stack_books[i])
              print()
ch = 0
while ch != 4 :
              print("1. Push")
              print("2. Pop")
              print("3. Display")
              print("4. To Exit ")
              ch = int(input("Enter Your choice : "))
              if ch == 1 :
                            book_no = int(input("Enter the Book No. to be Pushed : "))
                            book_name = input("Enter the Book Name to be Pushed : ")
                            list_pushed = [book_no,book_name]
                            Push(list_pushed)
              if ch == 2 :
                            if len(stack_books) == 0 :
                                          print("Empty Stack")
                            else :
                                          print("Popped Value :",Pop())
              if ch == 3 :
                            Display()
print("Thank You !")             
