"""
main.py
CST 2213
Project
David Xu (041173885)    
Description:
Contains driver code and Streamlit frontend
Note: To run the app, replace "[REDACTED]" with your values
"""

from src.utility import exception_decorator
import src.supermarket as supermarket
import src.customer as customer
from src.extraction import load
from src.preprocessing import product_preprocessing
from PIL import Image
import streamlit as st 

def main():

    #import supermarket inventory from file
    inventory_raw = load("data/Inventory.csv")
    inventory = product_preprocessing(inventory_raw)
    
    #import customer purchase history from file
    c1_purchases_raw = load("data/Customer1_Purchases.csv")
    c1_purchases = product_preprocessing(c1_purchases_raw)

    c2_purchases_raw = load("data/Customer2_Purchases.csv")
    c2_purchases = product_preprocessing(c2_purchases_raw)

    c3_purchases_raw = load("data/Customer3_Purchases.csv")
    c3_purchases = product_preprocessing(c3_purchases_raw)

    #Initialize Customer objects
    c1 = customer.Customer(1, "[REDACTED]", "[REDACTED]", "[REDACTED]", c1_purchases)
    c2 = customer.Customer(2, "[REDACTED]", "[REDACTED]", "[REDACTED]", c2_purchases)
    c3 = customer.Customer(3, "[REDACTED]", "[REDACTED]", "[REDACTED]", c3_purchases)

    #Initialize Supermarket object
    market = supermarket.Supermarket(inventory, [c1, c2, c3])


    # Set the page title and description
    st.set_page_config(
        page_title="Supermarket Personalized Ad Generator",
    )
    st.title("Supermarket Targeted Advertising Generator")
    st.image("./images/EmpressWalkLoblaws-Vivid.jpg", width=400)

    st.header("""
Generate a personalized advertisement for a customer to send by email and SMS""")

    #GUI CODE BELOW
    #drop down menu to select customer to generate ads for
    customers = []
    customer_names = []
    for i in market.get_customers():
        customers.append(({"name": i.get_customer_name(), "customer_id": i.get_customer_id()}))
 
    selected_customer = st.selectbox("Select customer: ", customers, format_func=lambda d: d["name"]) #format the dropdown menu with a lambda function
    st.write("Selected customer: ", selected_customer["name"])



    #radio button to select ad generation methodology
    methodology = st.radio("Select methodology: ", ("Generate based on supermarket inventory", "Generate based on comparing customers' purchase history"))

    if methodology == "Generate based on supermarket inventory":
        st.success("Generating ads based on supermarket inventory!")
    else:
        st.success("Generating ads based on comparing customers' purchase history!")

    #generate ad after selecting options
    #add formatting to ad for Streamlit display
    if(st.button("Generate Ad")):
        if methodology == "Generate based on supermarket inventory":
            ad = market.generate_ad_on_purchases(selected_customer['customer_id'])
            st.write("Generated ads for customer: ")
            st.write(ad)         
        else:
            ad = market.generate_ad_on_customers(selected_customer['customer_id'])
            st.write("Generated ads for customer: ")
            st.write(ad)             
            
if __name__ == '__main__':
    main()