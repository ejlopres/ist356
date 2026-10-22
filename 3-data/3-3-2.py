#### Who is not buying from minimart?
# You have been hired to build a UI to display names of customers who did not buy from minimart in any given month.
# Provide a Streamlit UI with a drop down selection for the month. (jan, feb, mar, apr)
# It then outputs a dataframe of customers who did not buy anything in that month. 
# **HINT**
# Access the raw data from this base url: `https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/`

import streamlit as st
import pandas as pd
import numpy as np
import requests

# Inputes and URls
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ["jan", "feb", "mar", "apr"]
selected = st.selectbox("Select a month", months)
monthly_urls = f"{base}purchases-{selected}.csv"
customer_urls = f"{base}customers.csv"

#Dataframes and Merges
orders = pd.read_csv(monthly_urls)
customers = pd.read_csv(customer_urls)
combined = pd.merge(customers, orders, left_on="customer_id", right_on="customer_id", how="left")

#Slight manipulation to make the data more accurate
combined_filtered = combined[combined['order_id'].isnull()]
combined_filtered = combined_filtered[['customer_id', 'firstname', 'lastname']]

#Outputs
# st.write(monthly_urls)
# st.dataframe(customers)
# st.dataframe(orders)
st.dataframe(combined_filtered)
