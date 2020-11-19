def odd_even(num):
    if num%2==0:
        return"even"
    else:
        return"odd"
print(odd_even(6))
#same code in 2 lines
OddEven=lambda num:print("Even") if num%2==0 else print("Odd")
OddEven(7)
#print(OddEven(5,6))
#function in one line when you want fast processing and less space storage
# machine learning m we want this thing because sometimes we donot want the function to take space.
print((lambda num:num**2)(8))
#map reduce& filter
num=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda num:num**2,num)))
print(list(filter(lambda num:num**3 if num%2==0 else None,num)))
from functools import reduce
print(reduce(lambda n,m:n+m,num,5))
#n=5(initialise) and m=5+num
print("pythton".split("t"))#t ko as separator pass krra h
#taki hum apne string ko list ki tarahantreat kr paye

