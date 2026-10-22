# ### Order total and history

# Write a streamlit to input an amount.

# create an "add to total" button to accumulate the amount in the total
# create a "clear" button to reset the session vars

# display the total and the history of each item entered 

# HINT: you'll need to manage a list for history!

import streamlit as st
st.title("order accumulator")

# initialize into session state
if 'total_order' not in st.session_state:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

amount = st.number_input("Enter an amount", min_value=0.0)
add_to_order = st.button("Add to order", type="primary")
clear_order = st.button("Clear order", type="secondary")

#order accumulation logic
if add_to_order:
    st.session_state.total_order += amount
    st.session_state.order_history.append(amount)

if clear_order:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

st.text(f"Total Order: {st.session_state.total_order}")

st.text(f"Order History: {st.session_state.order_history}")
