# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:05:37 2022

@author: Aleks
"""


import pandas as pd


#TASK 1. mport the .csv file as a dataframe
df = pd.read_csv('tr.csv')

import time

start = time.time()

# renaming data frame
result = df

# Splitting the string into pandas columns
result[['UserID', 'TransactionID', 'Year', 'Month', 'Day', 'Time', 'ItemCode', 'ItemDescription', 'NumberItems', 'CostPrice', 'SellingPrice','Country', 'Client Age']]= result['UserId;TransactionId;Year;Month;Day;Time;ItemCode;ItemDescription;NumberOfItemsPurchased;CostPerItem;SellingPricePerItem;Country;ClientKeywords'].str.split(";", n = 12, expand = True) 

# Cleaning data - removing unwanted symbol "["
result['Client Age'] = result['Client Age'].str.replace('[', '')

# TASK 7, Changing the ItemDescription column in the dataframe to lowercase
result['ItemDescription'] = result['ItemDescription'].str.lower()

#For TASKS 2, 3, 4 - converting strings into float numbers
result['NumberItems'] = result['NumberItems'].astype(float)
result['CostPrice'] = result['CostPrice'].astype(float)
result['SellingPrice'] = result['SellingPrice'].astype(float)

# TASK 2, creating CostPerTransaction column
result['CostPerTransaction'] = result['NumberItems'] * result['CostPrice']

# TASK 3, creating SalesPerTransaction column
result['SalesPerTransaction'] = result['NumberItems'] * result['SellingPrice']

# TASK 4, creating ProfitPerTransaction
result['ProfitPerTransaction'] = result['SalesPerTransaction'] - result['CostPerTransaction']

# TASK 5, raunding numbers to 2 decimals
result['ProfitPerTransaction']= result['ProfitPerTransaction'].round(decimals = 2)

#TASK 6, Changing the date format
result['Date'] = result['Day'].astype(str) + "-" + result['Month'].astype(str) + "-" + result['Year'].astype(str)

#TASK 8, Creating clients key words in 3 columns
result.columns = result.columns.str.replace('Unnamed: 1', 'ClientType')
result.columns = result.columns.str.replace('Unnamed: 2', 'LengthofContract')
result['LengthofContract'] = result['LengthofContract'].str.replace(']', '')


print(result.describe())


result = result[['UserId;TransactionId;Year;Month;Day;Time;ItemCode;ItemDescription;NumberOfItemsPurchased;CostPerItem;SellingPricePerItem;Country;ClientKeywords',
       'Date', 'Time' ,'ClientType', 'LengthofContract', 'Client Age' , 'Country','UserID', 'TransactionID', 'Year', 'Month',
       'Day', 'ItemCode', 'ItemDescription', 'NumberItems',
       'CostPrice', 'SellingPrice', 
       'CostPerTransaction', 'SalesPerTransaction', 'ProfitPerTransaction'
       ]]

print (result.columns)
result.to_csv('real7A.csv')

end = time.time()

print('TIME=', end - start)

print ('finish 7A')







