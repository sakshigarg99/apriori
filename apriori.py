# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:21:09 2020

@author: My
"""
#!pip install apyori

import pandas as pd
#import numpy as np
df= pd.read_csv('C:/Users/My/Downloads/Market_Basket_Optimisation.csv',header=None)

transactions=[]
for i in range(0,7501):
    transactions.append([str(df.values[i,j]) for j in range(0,20)])

from apyori import apriori
rules= apriori(transactions= transactions, min_support= 0.003,min_confidence= 0.2, min_lift= 3, min_length=2, max_length=2)

results= list(rules)
#print(results)

def inspect(results):
    lhs= [tuple(result[2][0][0])[0]for result in results]
    rhs= [tuple(result[2][0][1])[0]for result in results]
    support= [result[1]for result in results]
    confidence= [result[2][0][2]for result in results]
    lift= [result[2][0][3]for result in results]
    
    return list(zip(lhs, rhs, support, confidence, lift))

resultsdf= pd.DataFrame(inspect(results), columns=['left hand side','right hand side','support','comfidence','lift'])

print(resultsdf.nlargest(10, columns='lift'))