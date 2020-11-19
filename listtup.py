'''
homogenous as well as hetrogenous type: iterables
str   ""
list  []
tuple ()
dictionary {key:value}
set {}
'''
list1=[1,2.3,3,"44",6,5]
list2=['k','z','g','g','f']

print (list1,list2)
print(list1[4-1])
list1[3]=[10, 11]
print(list1)
print(list1[3][0])
print(list1[:4])
print(list1[::-1])
list1.append([45, 77, 8, 9])
print(list1)
print(list1.index(3))
list2.sort()
print(list2)
#list1.__getitem__()
print(list1)
list=[1,2,6,4,8,3,9]
list.sort()



'''
num=int (input("Enter the value 1: "))
num1=int (input("Enter the value 2: "))
num2=int (input("Enter the value 3: "))
if num>num1:
    if num>num2:
        print("{} is greatest.".format(num))
    else :
        print("{} is greatest.".format(num2))
elif num>num1:
    if num1>num2:
        print("{} is greatest.".format(num1))
    else:
        print("{} is greatest.".format(num2))
else:
    print("{} is greatest.".format(num2))
'''
'''
num=float(input("Enter the value to check odd or even? "))
if num%2==0 :
    print("Number is Even.")
elif num%2==1:
    print("Number is Odd.")
elif num%1==0:
    print("Number is bth odd & even") #only the cond satisfed 1st will be executed
else:
    print("Enter a valid number to check")
    '''
'''
l1={1,2,3,4}
l2={1, 2, 3, 4}
print (l1)
print (l2)
print(int("5"))

print(int(" 5"))
'''