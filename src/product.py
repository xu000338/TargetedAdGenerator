"""
product.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains code for Product class
"""

from .utility import exception_decorator

#Product stores all information related to a product
class Product:

    #Initialize Product object (int, string, string, string, string, float)
    @exception_decorator    
    def __init__(self, sku, brand, name, department, tier, price):
        self.sku = sku
        self.brand = brand
        self.name = name
        self.department = department
        self.tier = tier
        self.price = price

    #Returns sku (int)
    @exception_decorator    
    def get_sku(self):
        return self.sku

    #Returns brand (string)
    @exception_decorator    
    def get_brand(self):
        return self.brand

    #Returns name (string)
    @exception_decorator    
    def get_name(self):
        return self.name

    #Returns department (string)
    @exception_decorator    
    def get_department(self):
        return self.department

    #Returns tier (string)
    @exception_decorator    
    def get_tier(self):
        return self.tier

    #Returns price (float)
    @exception_decorator    
    def get_price(self):
        return self.price
        
    #Returns full product information as a formatted string
    @exception_decorator    
    def __str__(self):
        return str(self.sku) + " " + self.brand + " " + self.name + " " + self.department + " " + self.tier + " " + str(self.price)
