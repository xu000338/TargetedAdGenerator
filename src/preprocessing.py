"""
preprocessing.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains methods for data pre-processing
"""
from .product import Product
#import sys
#sys.path.insert(0, 'C:\Users\davex\Documents\College\CST2213\Project\Iteration_2\src')

from .utility import exception_decorator
'''
1. Load dataframe into list of product objects
2. Return list of products

'''
@exception_decorator
def product_preprocessing(df):
    
    list = []
    
    for i in range(len(df)):
        row = df.iloc[i]
        instance = Product(sku=row['SKU'], brand=row['Brand'], name=row['Name'], department=row['Department'], tier=row['Tier'], price=row['Price'])
        list.append(instance)
    #return list of products
    return list
