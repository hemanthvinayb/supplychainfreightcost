import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv(r'D:\Supply Chain Shipment Pricing Data\SCMS_Delivery_History_Dataset.csv')

inial_data=pd.read_csv(r'D:\Supply Chain Shipment Pricing Data\SCMS_Delivery_History_Dataset.csv')

zero_value=('0')
df['Freight Cost (USD)'].replace('Invoiced Separately',zero_value,inplace=True)
df['Freight Cost (USD)'].replace('Freight Included in Commodity Cost',zero_value,inplace=True)      
df['Weight (Kilograms)'].replace('Weight Captured Separately',zero_value,inplace=True)


import first_fun

df=first_fun.fun1(df)

df=first_fun.fun2(df)


Nan_value=float('NaN')
df['Freight Cost (USD)'].replace(0,Nan_value,inplace=True)

df['Weight (Kilograms)'].replace(0,Nan_value,inplace=True)

df=df.drop(['ID','Project Code','PQ #','PO / SO #','ASN/DN #','Vendor INCO Term',
            'PQ First Sent to Client Date','PO Sent to Vendor Date','Item Description',
            'Molecule/Test Type','Brand','Dosage Form','First Line Designation','Line Item Value',
            'Line Item Insurance (USD)','Dosage','Delivery Recorded Date', 'Delivered to Client Date',
            'Manufacturing Site','Vendor','Sub Classification','Managed By'],axis=1)


for column in ['Scheduled Delivery Date']:
        df[column] = pd.to_datetime(df[column])
        df[column + ' Year'] = df[column].apply(lambda x: x.year)
        df[column + ' Month'] = df[column].apply(lambda x: x.month)
        df[column + ' Day'] = df[column].apply(lambda x: x.day)
        df = df.drop(column, axis=1)
    


df=df.dropna(axis=0)

x_var=df.drop('Freight Cost (USD)',axis=1)
y_var=df['Freight Cost (USD)']

x_var['Country'] = pd.Categorical(x_var['Country'] )
x_var['Country'] = x_var['Country'].cat.codes

x_var['Product Group'] = pd.Categorical(x_var['Product Group'] )
x_var['Product Group'] = x_var['Product Group'].cat.codes


x_var['Shipment Mode'] = pd.Categorical(x_var['Shipment Mode'] )
x_var['Shipment Mode'] = x_var['Shipment Mode'].cat.codes

x_var['Fulfill Via'] = pd.Categorical(x_var['Fulfill Via'] )
x_var['Fulfill Via'] = x_var['Fulfill Via'].cat.codes



from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

x_train,x_test,y_train,y_test=train_test_split(x_var,y_var,random_state=0,test_size=0.25)

dt=RandomForestRegressor()
dt.fit(x_train,y_train)

print(dt.score(x_train,y_train))
print(dt.score(x_test,y_test))


from sklearn.metrics import mean_squared_error 
from math import sqrt

pred=dt.predict(x_test) #make prediction on test set
error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse

print(type((df['Freight Cost (USD)'][2])))

import pickle
# open a file, where you ant to store the data
file = open('random_forest_regression_model.pkl', 'wb')

# dump information to that file
pickle.dump(dt, file)


