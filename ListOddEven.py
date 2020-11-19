num=int(input("Enter a number till where you want your odd even numbers list: "))
i=1
odd=[]
even=[]
for i in range (i , num):
    if i%2==0:
        even.append(i)
        i+=1
    else:
        odd.append(i)
        i+=1
print(odd)
print(even)
