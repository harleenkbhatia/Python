import numpy as np

arr=np.array([1,2,3,4,5,6,7])
arr1=np.array([[[1,2,3],[4,5,5]]])
arr2=np.array([[[3,2,3],[4,5,5],[4,5,6]]])
arr7=np.array([[[1,1,5],[3,8,4],[2,3,7]]])
arr3=np.array([3,5,1])
print(type(arr))
print(arr1)
print(arr1.ndim)
print(arr.shape)
print(arr1.shape)

print(arr2.shape)
#(1,2,3) 1 is depth that is 1 ke 2x3 array h
#3d (3,5,1) (4,3,2,2)
arr4=np.array([[[4],[3],[5],[1],[6]],[[2],[3],[5],[4],[6]],[[4],[1],[2],[6],[7]]])
print(arr4)
#(4,3,2,2)
arr5=np.array([[[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]],
               [[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]],
               [[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]],
               [[[4, 2], [3, 2]],
               [[1, 5], [3, 4]],
               [[1, 2], [2, 6]]]])
print(arr5.shape)
print(arr.min())
print(arr.max())
print(arr.argmax()) #index value of the max no.
print(arr.prod())
print(arr.all())#checks whether all are non zero or not if yes then true if even 1 0 then false
print(arr.any())#checks whether all  are 0 or not if all are 0 then true otherwise false
print(arr4.shape)
print(np.arange(0,10,0.25)) #array in which you can set a range and sequence m you cn print
print(np.ones((3,4)))
a=np.full((3,6),7)
print(a.reshape((2,9,1)))
print(a.reshape(-1,1))
print(arr2.T)
print(arr2.transpose()) #two ways to transpose
#(4,3,2,2)
arr5=np.array([[[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]],
               [[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]],
               [[[4,2],[3,2]],
               [[1,5],[3,4]],
               [[1,2],[2,6]]]])
print(arr5.shape)

#arr5.reshape((1,3,2,2))
#arr5.reshape((1,)+arr5.shape)
#print(arr5)
#print(arr5.shape)
print(arr2.dot(arr3))
print(np.concatenate((arr2,arr7),axis=1))
b=np.arange(0,10,0.25).reshape((10,4))
b[7,1]=7.75
print(b.shape)
print(b[1])
print(b[2])
print(b[3])
#print(help(b.tofile))
#b.tofile("numpy.data.txt",sep=',')
'''
x,data=np.loadtxt("numpydata.txt",delimiter=',')
print(data)
'''