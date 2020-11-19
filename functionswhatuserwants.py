#add multiplication subtract division floor div mod
def sum():
    X=int(input("Enter num1 : "))
    Y=int(input("Enter num2 : "))
    print("sum=",X+Y)
def product():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X * Y)
def subtract():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X - Y)
def division():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X / Y)
def modulus():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X % Y)
def floor():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X // Y)
def power():
    X = int(input("Enter num1 : "))
    Y = int(input("Enter num2 : "))
    print("sum=", X ** Y)
def adam():
    X = int(input("Enter a no. to check the given no. is adam or not : "))
    sq = str(X ** 2)
    rev = int(sq[::-1])
    sqr = int(rev ** (0.5))
    sqrr = str(sqr)
    reverse = int(sqrr[::-1])
    if reverse == X:
        print("The given no. is an Adam's Number.")
    else:
        print("The given no. is not an Adam's Number")
def fibonacci():
    X = int(input("enter number of elements you want to see fibonacci series till: "))
    a, b = 0, 1
    i = 0
    if X == 1:
        print(a)
    else:
        print("fibonacci series:")
        for i in range(i, X):  # while i < num:
            print(a)
            c = a + b
            a = b
            b = c
            i += 1
def prime():
    X = int(input('Enter a no. to check it is prime or not : '))
    flag = 0

    if X > 0:

        n = int(X / 2)
        for i in range(1, n):
            if flag < 2:
                if X % i == 0:
                    flag += 1
            else:
                i = n
        if flag >= 2:
            print("given no. is not a prime no.")
        else:
            print("given no. is a prime no.")
def primerange():
    X=int(input("Enter value of no. you want to see prime nos. till : "))
    i=1
    for i in range(1,X):
        for i in range(2, X):
            if (X % i) == 0:
                print(X, "is not a prime no.")
                i += 1
                break
            else:
                print(X, "is a prime no.")
                break

def table():
    X = int(input("Enter value you want to see table of:"))
    i = 1
    for table in range(i, 11):
        b = i * X
        print("{} * {} = {}".format(X, i, b))
        i += 1
def tablerange():
    X = int(input("Enter value of no. you want to see tables till:"))
    j = 1
    for j in range(j, X + 1):
        print("Table of {}".format(j))
        i = 1
        for table in range(i, 11):
            b = i * j
            print(" {} * {} = {} ".format(j, i, b))
            i += 1
        j += 1
print("type\n"
      "1 for sum\n "
      "2 for product\n"
      "3 for subtract\n"
      "4 for modulus\n"
      "5 for division\n"
      "6 for floor division\n"
      "7 for power\n"
      "8 for adam\n"
      "9 for table\n"
      "10 for tablerange\n"
      "11 for fibonacci\n"
      "12 for prime\n"
      "13 for primerange\n")
Operation=int(input("Enter the operation you want to perform: "))
if Operation==1:
    sum()
elif Operation==2:
    product()
elif Operation==3:
    subtract()
elif Operation==4:
    modulus()
elif Operation==5:
    division()
elif Operation==6:
    floor()
elif Operation==7:
    power()
elif Operation==8:
    adam()
elif Operation==9:
    table()
elif Operation ==10:
    tablerange(0)
elif Operation==11:
    fibonacci()
elif Operation ==12:
    prime()
elif Operation==13:
    primerange()
