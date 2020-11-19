import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv('C:/Users/Jagdeep/Downloads/xclara.csv')
clusters=3
kmean=KMeans(n_clusters=clusters)
kmean.fit(data)
center=kmean.cluster_centers_
y=kmean.predict(data)
print(kmean.cluster_centers_)

#print(kmean.predict([data.iloc[0,:]]))
#print(set(kmean.predict(data)))
plt.scatter(center[:,0],center[:,1])
plt.scatter(data['V1'],data['V2'],c=y)
plt.xlabel('V1')
plt.ylabel('V2')
plt.title("Cluster numbe: {}".format(clusters))
plt.show()
