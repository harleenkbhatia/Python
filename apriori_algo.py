import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

dataset=[
    ['milk','onion','yogurt','eggs'],
    ['chips','tomatoes','honey','eggs'],
    ['kidney beans','daal','unicorn','apple'],
    ['chips','onion','honey','corn'],
    ['chips','onion','corn','honey']
]
te=TransactionEncoder()
te_array=te.fit(dataset).transform(dataset)  
df=pd.DataFrame(te_array,columns=te.columns_)
print(df)
from mlxtend.frequent_patterns import apriori
apriori_data=apriori(df,min_support=0.001,use_colnames=True)
#ek row m repeat ni krna
apriori_data['Length']=apriori_data['itemsets'].apply(lambda x:len(x))
print(apriori_data)

print(apriori_data[(apriori_data['Length']==2) & (apriori_data['support']>=0.2)])