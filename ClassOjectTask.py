'''
class Student:
    num=0
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
        Student.num+=1
        print("{} marks entered".format(Name))
Student1=Student("xyz",88)
Student2=Student("jf",40)
Student3=Student("jak",80)
Student4=Student("xer",90)
Student5=Student("xom",67)
Student6=Student("jef",55)
Student8=Student("james",77)
print("num of students in class are : ",Student.num)
'''
class I:
    def __init__(self,sno):
        self.sno = int(sno)
        print("Object Created")
class H:
    def __init__(self,name):
        self.name = name
        print("Object Created")
class G:
    def __init__(self,roll):
        self.roll = int(roll)
        print("Object Created")
class F(H,I):
    def __init__(self,phn,name,sno):
        self.phn = int(phn)
        H.name = name
        I.sno = sno
        print("Object Created")
class E:
    def __init__(self,std):
        self.std =std
        print("Object Created")
class J(E,F,G):
    def __init__(self,books,std,phn,roll):
        self.books=books
        E.std = std
        F.phn = phn
        G.roll = roll
        print("Object Created")
class D:
    def __init__(self,address):
        self.address = address
        print("Object Created")
class C:
    def __init__(self,position):
        self.position=position
        print("Object Created")
class B(C,D):
    def __init__(self,year,position,address):
        self.year=year
        C.position = position
        D.address = address
        print("Object Created")
class A(B,J):
    def __init__(self,semester,year,position,address,std,phn,roll,name,sno,books):
        self.semester=semester
        B.year=year
        C.position=position
        D.address=address
        E.std=std
        F.phn=phn
        G.roll=roll
        H.name=name
        I.sno=sno
        J.books=books
        print("Object Created")

    def display(self):
        print("Currently in semester:", self.semester)
        print("Currently in year:", self.year)
        print("Position in Class:", self.position)
        print("Address:", self.address)
        print("Standard:", self.std)
        print("Phone no.:", self.phn)
        print("Roll  No.:", self.roll)
        print("Name:", self.name)
        print("sno:", self.sno)
        print("Num of Books on rent:", self.books)

bcd=B("2nd year","1st pos","Gupta Colony")
a=A("4th sem","2nd year","1st pos","Gupta Colony","IT1",1234567891,33,"Harleen",1,12)
A.display(a)
jefg=J("12 Books on rent","IT1",1234567891,33)