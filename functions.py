def message ():
    print("this is ml class")
message()
def pow(x,y):
    return(x**y) #print(x**y) khi save ni hora tha
a=pow(9,3)
print("cube of 9 is {}".format(a))
def subtract(x=4,y=2):#creating func with by default values
    return(x-y)
a=subtract(y=6,x=8) #a=subtract(6,8) ye -2 dega
print("difference is {}".format(a))
#HCF x=ab+r
print(subtract(5,1))

def multipleAddition(*var):#to get multiple inputs from user without assigning keys
    product=1#0 for sum
    for item in var:
        product*=item
    print("product of given nos. =",product)
    print(sum(var))#without loop
multipleAddition(2,3,6,8,9,10,5,22)#tupple
def multipleKey(**var):#to get multiple inputs with keys
    for keys, values in var.items():
        print("key is : {} value is : {}".format(keys,values))
multipleKey(x=1, y=2, z=8)  # dictionary
