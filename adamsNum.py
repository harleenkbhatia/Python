a= int(input("Enter a no. : "))
sq = str(a**2)
print(sq)
rev = int(sq[::-1])
print(rev)
sqr = int(rev**(0.5))
sqrr = str(sqr)
print(sqr)
reverse = int(sqrr[::-1])
print(reverse)
if reverse == a :
    print("The given no. is an Adam's Number.")
else :
    print("The given no. is not an Adam's Number")

