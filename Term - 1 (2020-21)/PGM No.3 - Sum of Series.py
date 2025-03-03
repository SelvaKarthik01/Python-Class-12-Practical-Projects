# Printing Sum of the Series 
print("""Sum of Series : 
1+1/1!+1/2!+1/3!+⋯+1/n!""")
print("*************************************************************** ")
n = int(input("Enter the Value for N to Evaluate the Sum of Series : "))
s = 1
print(1,end = " ")
for i in range(1,n+1):
              p = 1
              for j in range(i,0,-1):
                            p *= j
              a = 1/ p
              s += a
              print(" + ","1 / ",i,"!",end = " ")
print("=" ,s)
