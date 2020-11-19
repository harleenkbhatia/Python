#inline
x=int(input("enter a value of x coordinate : "))
y=int(input("enter a value of y coordinate : "))
z=int(input("enter a value of z coordinate : "))
n=int(input("enter a number n : "))
i=0
j=0
k=0
co=[[i,j,k] if i+j+k != n else None for i in range (x+1) for j in range (y+1)  for k in range (z+1) ]
print(co)
'''
x=int(input("enter a value of x coordinate : "))
y=int(input("enter a value of y coordinate : "))
z=int(input("enter a value of z coordinate : "))
n=int(input("enter a number n : "))
i=0
j=0
k=0
for i in range (i,x):
    for j in range (j,y):
        for k in range (k,z):
            print(i,j,k)
            i+j+k != n
'''