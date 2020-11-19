num=int(input("enter number of elements: "))
a,b=0,1
i=0
if num==1:
    print(a)
else:
    print("fibonacci series:")
    for i in range(i,num): #while i < num:
        print(a)
        c=a+b
        a=b
        b=c
        i+=1

