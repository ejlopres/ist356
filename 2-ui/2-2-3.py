
# ### Order File processing

# Write a streamlit to input a text file with one line per order. Samples are provided in the `data` folder, but each line should have the amount of the order.

# output the number of orders and the total amount of all orders.

import streamlit as st
st.title("File Order Processor")

selected_file = st.file_uploader("Select a file to process:", type=["txt"], key="file_uploader")

total = 0.0
count = 0

if selected_file is not None:
    content = selected_file.read().decode("utf-8")
    for line in content.splitlines():
        number = float(line.strip())
        total += number
        count += 1


st.markdown(f"""
### File processing results
 - total: {total}
 - count: {count}
""")