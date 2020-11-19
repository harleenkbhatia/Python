#input
#adam no. in one array non adam no. in second array
num=int(input("Enter a no. till where you want to get the adam nos.: "))
a=0
for a in range (0,num+1):
    sq = str(a**2)
    rev = int(sq[::-1])
    sqr = int(rev**(0.5))
    sqrr = str(sqr)
    reverse = int(sqrr[::-1])
    if reverse == a :
        print("{}".format(a))
    else :
        None