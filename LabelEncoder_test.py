import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/Users/Jagdeep/Downloads/mushrooms.csv")
lab=LabelEncoder()
data['class']=lab.fit_transform(data['class'])
data['cap-shape']=lab.fit_transform(data['cap-shape'])
data['cap-surface']=lab.fit_transform(data['cap-surface'])
print(data.head())
print(data['class'].unique())
print(data['cap-shape'].unique())
print(data['cap-surface'].unique())
