import pandas as pd 
import numpy as np

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

df= pd.read_csv(r"C:\Users\hp\Desktop\New folder\Project\Data\flats - flats.csv",encoding='latin1')
print(df.sample(5))

# shape
print(df.shape)
# info
print(df.info())

# check for duplicates
print(df.duplicated().sum())

#check for missing values

print(df.isnull().sum())

# Removing the column which is not use ful i.e link of the websit, property id 
df.drop(columns=['link','property_id'], inplace=True)
print(df.head())

# Renmae columns

df.rename(columns={'area':'price_per_sqft'},inplace=True)

#society
print(df['society'].value_counts())
print(df['society'].value_counts().shape)

# Eliminating the society name which make an extra category by inluding the rating 
import re
df['society']=df['society'].apply(lambda name: re.sub(r'\d+(\.\d+)?\s?[?★]','',str(name)).strip()).str.lower()
print(df['society'].value_counts())
print(df['society'].value_counts().shape)

# Now we will check for the price wala coulumn kuch price lac mai luch crore me likhe hue hai

print(df['price'].value_counts())
print(df['price'].value_counts().shape)

# we will drop all the rows which has not mentioned about the price instead of that price on request is written

df=df[df['price'] != 'Price on Request']
print(df['price'].value_counts().shape)

# Now we convert the lac into crore
def treat_price(x):

    if type(x)== float:
        return x
    else:
        if x[1] =='Lac':
            return round(float(x[0])/100,2)
        else:
           return round(float(x[0]),2)

df['price']=df['price'].str.split(' ').apply(treat_price)
print(df.head())