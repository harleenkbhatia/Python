
import Calculator as cal
def Maths():
    X,Y=int(input("enter value of X: ")),int(input("Enter value of Y: "))
    print(cal.subtract(X,Y))
    print(cal.division(X,Y))
    print(cal.floor(X,Y))
    print(cal.modulus(X,Y))
    print(cal.power(X,Y))
    print(cal.product(X,Y))
    print(cal.adam(X))
    print(cal.fibonacci(X))
    print(cal.prime(X))
    print(cal.table(X))
    print(cal.tablerange(X))
Choice=int(input("Choose 1 for Maths Calc and 2 for Login and anyother no. for Signup: "))
if Choice==1:
    Maths()
elif Choice==2:
    print(cal.Login())
else:
    print(cal.Signup())