class fruit:
    #function ko class m bolte h methods. ek method ke ek argument ko ussi class ke dusre
    # method m call krna is called linking self.fruitname
    def __init__(self, fruitname, quantity):#arguments h fruitname, quality
        self.fruitname=fruitname
        self.quantity=quantity
        print("Object Created")#classes ko ojects bnake call krte h
    def message(self):
        print("the fruit name is : {}".format(self.fruitname))
        print("the quantity of fruits is : {}".format(self.quantity))
class apple(fruit):#inheritance of fruit class in apple
    __email=("harleen12")#__ hides data
    def __init__(self,colour,fruitname,quantity):
        fruit.__init__(self,fruitname,quantity)
        self.colour=colour
        print("apple object created")
    def messagee(self):
        print("the colour of apple is : {}".format(self.colour))
Data= fruit("Mango",3) #object
print(Data.quantity)
print(Data.fruitname)
Data.message()
#print(Data.fruitname) #none agr aap func ke andr already print krrhe ho toh ho print ka return type is none
applecolour= apple("red","apple",5)
print(applecolour.colour)
applecolour.messagee()
applecolour.__setattr__("colour","green")
print(applecolour.colour)
applecolour.messagee()
print(applecolour.fruitname)
print(applecolour._apple__email)#accessing data hidden

#local var sirf ek func m global everywhere