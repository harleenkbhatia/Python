a=int(input("Enter a no. till where you want to see prime no."))
for num in range (2,a+1):
    if num>0:
        for i in range (2,num):
            if num%i==0:
                None
                break
        else:
            print("{}".format(num))
'''
#without break statement
num= int(input('Enter a no. to check it is prime or not : '))
flag =0

if num>0:
    for i in range(1, num):
        if flag<2 :
            if num % i == 0:
                flag+= 1
        else:
            i=num
    if flag>=2:
        print("given no. is not a prime no.")
    else:
        print("given no. is a prime no.")
'''
#for loop
'''
num=int(input('Enter a no. to check it is prime or not: '))
for i in range(2,num):
    if (num%i)==0:
        print(num, "is not a prime no.")
        i+=1
        break
    else :
        print(num,"is a prime no.")
        break
else:
    print(num, "is a prime no.")
#while loop

num= int(input('enter a no. to check it is prime or not: '))
i=2
while i<num :
    if (num%i)==0:
        print (num,"is not a prime number")
        i+=1
        break
    else :
        print(num,"is a prime number")
        break
else:
    print (num,"is a prime number")
'''
