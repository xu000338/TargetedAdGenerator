"""
supermarket.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains code for Supermarket class
Note: To run the code, replace "[REDACTED]" with your own values
"""
from .customer import Customer
from .product import Product
from .utility import exception_decorator
import smtplib
from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import sample 
from twilio.rest import Client


#Supermarket class (all supermarket operations functions are here)
class Supermarket:

    #Initialize Supermarket object ([Products], [Customers])
    @exception_decorator
    def __init__(self, products, customers):
        self.inventory=products
        self.customers=customers

    #Add a products to supermarket's inventory 
    @exception_decorator    
    def load_products(self, products):
        self.inventory = products

    #Return the supermarket's inventory (list of Products)
    @exception_decorator    
    def get_inventory(self):
        return self.inventory

    #Lookup a product by sku (Product)
    @exception_decorator    
    def get_product(self, sku):
        for i in self.inventory:
            if i.get_sku() == sku:
                return i
                
    #Lookup a customer by cust_id
    @exception_decorator    
    def get_customer(self, cust_id):
        for i in self.customers:
            if i.get_customer_id()==cust_id:
                return i

    #Return a list of all the supermarket's customers (list of Customers)
    @exception_decorator    
    def get_customers(self):
        return self.customers
    
    #Send personalized email containing generated ad
    @exception_decorator
    def send_email(self, advertisement, cust_id):
        
        cust_name = self.get_customer(cust_id).get_customer_name()
        cust_email = self.get_customer(cust_id).get_customer_email()
        
        msg = EmailMessage()
        msg["Subject"] = "Hello " + cust_name + "! Here are your personalized ads: "
        msg["From"] = "[REDACTED]"
        msg["To"] = cust_email
        msg.set_content(advertisement)
    
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("[REDACTED]", "[REDACTED]")
            server.send_message(msg)
    
    #Send personalized SMS message containing generated ad
    @exception_decorator
    def send_SMS(self, advertisement, cust_id):
    
        cust_name = self.get_customer(cust_id).get_customer_name()
        cust_phone_number = self.get_customer(cust_id).get_customer_phone_number()
        
        
        account_sid = "[REDACTED]"
        auth_token = "[REDACTED]"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body = "Hello, " + cust_name + "! You might like these products: " + advertisement,
        from_="[REDACTED]",
        to=cust_phone_number
        )
    
    #Generate personalized ads based on a customer's purchase history
    @exception_decorator
    def generate_ad_on_purchases(self, cust_id):

        #prepare ad string
        ad_str = "Suggested products for you: " + "\n"
        ad_list = []

        #get the customer's purchases from their cust_id
        customer_purchases = self.get_customer(cust_id).get_purchases()
            
        #iterate through a customer's purchases and compare it to the supermarket's inventory,
        #looking for similarities in purchased brands and tier levels between the two datasets.
        for i in customer_purchases:
            for j in self.get_inventory():
                if i.get_sku() != j.get_sku():
                    if (i.get_tier() == j.get_tier()) and (i.get_department() == j.get_department()):
                        ad_list.append(j.get_brand() + " " + j.get_name() + " " + str(j.get_price()))

        #if len(ad_list) > 10 then abbreviate  
        if len(ad_list) > 10:
            abbr_list = sample(ad_list, 10)
            ad_list = abbr_list    
     
        #format the ad string
        ad_list_to_str='\n'.join(ad_list)
        ad_str+=ad_list_to_str
        
        #invoke email sending function
        self.send_email(ad_str, cust_id)     
        
        #invoke SMS sending function
        self.send_SMS(ad_str, cust_id)    
        
        #return the formatted personalized ad -- customer should only see information relevant to them (no SKU number or internal metadata)
        return ad_str

        
    #Generate personalized ads based on similarity between a target customer's purchase history with other customers' purchase history
    @exception_decorator
    def generate_ad_on_customers(self, target_id):

        ad_str = "Other customers like you are buying: " + "\n"
        ad_list = []

        #get the customer's purchases from their cust_id
        customer_purchases = self.get_customer(target_id).get_purchases()

        #iterate through the target customer's purchases and compare it to other customers' purchases,
        #looking for correlations between the target customer's and other customers' purchases
        for i in customer_purchases:
            for j in self.get_customers():
                for k in j.get_purchases():
                    if i.get_sku() == k.get_sku():
                        for l in j.get_purchases():
                            if (i.get_sku() != l.get_sku()):
                                if (i.get_tier() == l.get_tier()) or (i.get_department() == l.get_department()):
                                    ad_list.append(l.get_brand() + " " + l.get_name() + " " + str(l.get_price()))

        #delete any duplicates
        ad_list = list(dict.fromkeys(ad_list))

        #if len(ad_list) > 10 then abbreviate  
        if len(ad_list) > 10:
            abbr_list = sample(ad_list, 10)
            ad_list = abbr_list    

        #format the ad string
        ad_list_to_str='\n'.join(ad_list)
        ad_str+=ad_list_to_str
                
        #invoke email sending function
        self.send_email(ad_str, target_id)  

        #invoke SMS sending function
        self.send_SMS(ad_str, target_id)
            
        #return the formatted personalized ad -- customer should only see information relevant to them (no SKU number or internal metadata)
        return ad_str
