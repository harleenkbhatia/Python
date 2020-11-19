a= int(input("Enter value:"))
j=1
for j in range(j,a+1):
    print("Table of {}".format(j))
    i=1
    for table in range(i,11):
        b = i * j
        print(" {} * {} = {} ".format(j, i, b))
        i+=1
    j+=1
