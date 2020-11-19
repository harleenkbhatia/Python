#set is created in {} maths vle sets hote h ye bi or set koi function ni h.
set1={2,3,4,5,8,68,8,2,4,99,45}
set2={7,5,6,4,9,10,3,2,5,3,4,5,6}
print(set1) #duplicate values are not found sets are used to remve duplicacy.
print(type(set1))
print(set([0,0,0,0,0,0,1,1,1,1,1,1,3,4,4,4,]))
print(set1.union(set2))
print(set1.intersection(set2))
set1.update({11,22,44,11,3,2}) #donot depend for order on set without sorting
print(set1)
set1.remove(3)
print(set1)
set1.