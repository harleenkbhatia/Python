import pandas as pd

#series dataframe
data=pd.read_csv('C:/Users/Jagdeep/Downloads/datasets_527325_1205308_Time.csv')
print(data.tail())
data['negative']=data['nagative'].apply(lambda x:0 if x=='' else x)
data['negative']=data['confirmed'].apply(lambda x:1 if x=='' else x)
'''
series=pd.Series([1,24,32,2,13,1,33],index=[10,20,30,40,50,60,70],name="Values")
print(series)
series=series.apply (lambda num: num**2 )
print(series)
#in form of dictionaries
df=pd.DataFrame({"a":[1,2,3],'b':[4,5,6],'c':[7,8,9]},index=['first','second','third'])
print(df)
print(df['b'][2])
print(df.iloc[0,:])
print(df.loc['third',:])
print(df.iloc[1,:])
print(df.loc['second':'third','a':'b'])
#in form of matrices
df2=pd.DataFrame([[1,4,5],[2,5,6],[4,8,9]],index=['first','second','third'],columns=['a','b','c'])
print(df2)
print(type(df['b']))#series data
#collection of multiple series is called data frame
print(df.head(1))#jb data top se chahiye
print(df.tail(1))#jb last se check krni ho
print(df.shape)
print(df.drop(['a','c'],axis=1))#for deleting
print(df.drop("third"))

df['a'][0]=3
print(df)
print(df.drop_duplicates(['a'])) #drops the duplicate one
#used to store data in excel
df.to_csv("data_df.csv")
#df.to_excel #same as above
data=pd.read_csv("data_df.csv")
print(data)
data=pd.read_csv('data_df.csv',index_col='Unnamed: 0')
print(data)
#data=data.drop('Unnamed: 0',axis=1)
#print(data)
print(data.columns)
#data=pd.read_csv('data_df.csv',index_col='Unnamed: 0',nrows=0)
#print(data.info())#memory usage
data=pd.read_csv('data_df.csv',index_col='Unnamed: 0')
print(data.describe())#description of memory
df.to_csv("data_df.csv",index=False)
'''