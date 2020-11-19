'''
def hcf(x,y):
    if x>y:
        r=x%y
        if r!=0:
            hcf(y,r)
        else:
            print("hcf is =",y)
    else:
        r=y%x
        if r!=0:
            hcf(x,r)
        else:
            print("hcf is =",x)

x = int(input("Enter no. to check HCF: "))
y = int(input("Enter no. to check HCF: "))
hcf(x,y)
'''    
X=int(input("Enter no. to check HCF: "))
Y=int(input("Enter no. to check HCF: "))
def hcf ():
    if X>Y:
        small=Y
    else:
        small=X
    for i in range(1,small+1):
        if((X%i==0) and (Y%i==0)):
            HCF=i
    return(HCF)
print("HCF is",hcf())
