dictionary={"a":4,"b":5,"c":7,4:8}
print(dictionary["b"]) #gives you value of key b sliced
print(dictionary.keys()) #returns tuple of keys
print(dictionary.values()) #returns tuple of values
print(dictionary.items()) #returns tuple of items

for keys, values in dictionary.items():
    print("key is : ",keys)
    print("value is : ",values)
#task in one way
index=0
for char in ("harleen") :
    print(char*index)
    index+=1

#task using enumerate
for index, char in enumerate(["harleen", "kaur", "bhatia"]):
    print(char*index)
else:
    print("task done")
dictionary1={1:3, 2:4, 8:3}
for i,v in dictionary1.items():
    print("key is",i, "value is",v)
    print(i*v)
dictionary.update({"d":5, "e":8, "f":9})
print(dictionary)
dictionary.popitem() #automatically last vli remove hojati h
print(dictionary)
dictionary.pop("d")
print(dictionary)
print(dictionary.fromkeys("p",8))
print(dictionary.copy()) #returns you copy of the dictionary
print(dictionary.get("a"))#returns the value of key and if no value then none.
print(dictionary.clear())