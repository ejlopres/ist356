import streamlit as st
import pandas as pd
import numpy as np
import requests

#use request to read in this as json data
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employees_data = response.json()

st.write(employees_data)

#loop over each key create a dataframe for each key and display it
for key in employees_data.keys():
    st.write(f"Data for {key}:")
    df = pd.DataFrame(employees_data[key])
    st.dataframe(df)

dfs = []
for key in employees_data.keys():
    df = pd.DataFrame(employees_data[key])
    df['department'] = key
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined Data:")
st.dataframe(combined_df)

filename = "3-data/data/combined_employees.jsonl"
combined_df.to_json(filename, orient="records", lines=True)
st.write(f"Combined data saved to {filename}")