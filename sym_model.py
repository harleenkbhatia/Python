from sklearn.datasets import load_iris
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
data=load_iris()
x=data.data[:,:2]
y=data.target

svme=SVC(gamma=0.001).fit(x,y) #gamma ki val jitni choti hoti h utna acha hota h
x_min, x_max, y_min,y_max,=x[:,0].min()-1,x[:,0].max()+1,x[:,1].min()-1,x[:,1].max()+1,
h=(x_max/x_min)/100
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arrange(y_min,y_max,h))
z=svm.predict(np.c_[xx.rave(),yy.ravel()]).reshape(xx.shape)
plt.contourf(xx,yy,z,cmap)
