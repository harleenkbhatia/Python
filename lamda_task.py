'''
#to check any one no. is prime or not
a = int(input("Enter a no. to check it is prime or not: "))

i = range(2, a)

file = open("prime.txt", 'w')

list(map(lambda j:print(" Not a prime no. ") if a%j==0 else print("{}".format( a )),i))

file.close()
'''
'''
num = int(input("enter a positive no. till where you want to see prime nos. : "))

i= range(2, num+1)
#lambda i: i if num>0 else print("Enter a valid no.")
j= range(2, num)
b=range(2,num+1)
a= i.index(c)
file = open("prime.txt", 'w')
#print(list(filter(lambda b:b if b<num else None,i)))
list(map(lambda k : print(" not a prime no. ") if a % k ==0 else print("{}".format(i)),i))
file.close()
'''
a=int(input('Enter a positive no. till where you want to see prime nos. :'))
num=[range(2,a+1)]
i=[range(a,2)]
#lambda k:num if num>0 else print("enter a valid no.")
filter(lambda k,b: None if k%b==0 else print("{}".format(num),num),i)




'''
for num in range (2,a+1):
    if num>0:
        for i in range (2,num):
            if num%i==0:
                None
                break
        else:
            print("{}".format(num))
'''