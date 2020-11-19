print("pythton".split("t"))#t ko as separator pass krra h
#taki hum apne string ko list ki tarahantreat kr paye
#newway to write for loop
print([i for i in range(10)])
#starting vala i is output or ye for loop ka kaam krra h but 10 times faster or in one line.
print([i**2 if i%2==0 else i**3 for i in range(10)]) #for inline loop
print([i**2 if i%2==0 else i**3 if i%2==3 else i**4 for i in range(10)])#how to use elif part in inline loop
#nested for loop
print([i+j for i in range(10) for j in range(10)])
num=int(input("Enter num you want to check prime or not:"))
print([ print("{} is not prime".format(i)) if(num%i)==0 else print("{} is prime.".format(i)) for i in range(2,num+1)])
print([i+j])
'''
import time
t1=time.time()
out=[]
for i in range(100):
    out.append(i)
    print(out)
t2=time.time()
print([i for i in range(100)])
t3=time.time()
#starting vala i is output or ye for loop ka kaam krra h but 10 times faster or in one line.
print(t1)
print(t2)
print(t3)
'''