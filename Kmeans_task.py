import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv('C:/Users/Jagdeep/Downloads/datasets_14701_19663_CC GENERAL2.csv')

dataa=data.apply(lambda x:0 if "" else x)

clusters=10
kmean=KMeans(n_clusters=clusters)
kmean.fit(dataa)
center=kmean.cluster_centers_
y=kmean.predict(dataa)
print(kmean.cluster_centers_)

#print(kmean.predict([dataa.iloc[0,:]]))
#print(set(kmean.predict(dataa)))
plt.scatter(center[:,0],center[:,1])
plt.scatter(dataa['BALANCE'],dataa['BALANCE_FREQUENCY'],c=y)
plt.xlabel('BALANCE')
plt.ylabel('BALANCE_FREQUENCY')
plt.title("Cluster number: {}".format(clusters))
plt.show()
