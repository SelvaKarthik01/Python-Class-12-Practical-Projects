# Linear Search in a Sequence
print("Linear Search")
print("*************************************************************** ")
L = eval(input("Enter the List of Elements to be Searched : "))
el = eval(input("Enter the Element to be Searched : "))
for i in range(len(L)):
              if L[i] == el :
                            print(el , "is Found at the Position : ",i+1)
                            print(el, "its Index No. is : ",i)
                            break
else :
              print(el , "is not Found in the Given List ")

                                          
