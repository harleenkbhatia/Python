#without using list
num=int(input("enter num till where you want to see your odd even list: "))
i=1
#file = open("even.txt", 'w')
for i in range(i,num+1):
    if i%2==0:
        file = open("even.txt", 'a')
        file.write("{} \n".format(i))
        file.close()
    else:
        file = open("odd.txt", 'a')
        file.write("{} \n".format(i))
        file.close()

'''
#using list
file=open("data.txt",'w')
num=100
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
OddList=str(odd)
EvenList=str(even)
file.writelines(OddList)
file.write("\n")
file.writelines(EvenList)
file.close()
'''
