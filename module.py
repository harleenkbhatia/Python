#package
# package and module ko call krne ka tareeka same h import krke krna hota h
# calculator is a module use call krke u cn use it
# package has collection of modules
# module means ek single unit.
# pythonfile pe jake module create kr skte h but package pe jakr
# vo poora package bnadega mtlb folder type ex arithmatic operations
# package ka symbol is directory ka symbol.
from ArithematicOperation.Calculator import subtract,product,floor as f
X,Y=int(input("enter value of X: ")),int(input("Enter value of Y: "))
print(f(X,Y))
print(product(X,Y))
print(subtract(X,Y))
