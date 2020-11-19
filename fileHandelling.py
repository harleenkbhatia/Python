#reading mode m file=open("demo.txt",'r')
# writing mode m file=open("demo.txt",'w')
# append mode m file=open("demo.txt",'a')
# similarly for binary mode binary read 'rb' binary write 'rw' binary append 'ra' may be)
#by defauld vo reading mode m open hoti h
file=open("demo.txt",'w')#by default empty file open krdega
#gonna make an object which will
file.write('Hello class\n')#value str honi chiye
file.write('hello ml\n')
file.writelines(["hello\n",'my\n','name\n','is\n','Harleen.\n'])
print(file.writable())
print(file.readable())
file.close()

file=open("demo.txt",'r')
print(file.read(20)[-5:])
print(file.readlines())
file.close()

file=open('demo.txt','a')
file.writelines(["1\n","2\n","3\n","4\n"])
file.close()
#with statement is used for using the file without closing the file.
'''
with open('as.txt','w') as file:
file.write('hello world')
'''