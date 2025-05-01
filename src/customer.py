"""
customer.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains code for Customer class
"""
from .utility import exception_decorator

#Customer class (stores all information related to a customer)
class Customer:

    #Initialize Customer object
    @exception_decorator
    def __init__(self, cust_id, name, email, phone_number, purchases):
        self.cust_id = cust_id
        self.cust_name = name
        self.email = email
        self.phone_number = phone_number
        self.purchases = purchases

    #Return cust_id 
    @exception_decorator
    def get_customer_id(self):
        return self.cust_id

    #Return cust_name
    @exception_decorator
    def get_customer_name(self):
        return self.cust_name
    
    #Return email
    @exception_decorator
    def get_customer_email(self):
        return self.email
    
    #Return phone_number
    @exception_decorator
    def get_customer_phone_number(self):
        return self.phone_number
    
    #Return list of customer's purchases
    @exception_decorator
    def get_purchases(self):
        return self.purchases
