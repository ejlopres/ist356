import streamlit as st

st.title ("Rectangle Calaculator")
length = st.number_input("Length of rectangle", min_value=0.0, max_value=100.0, step=0.1)
width = st.number_input("Width of rectangle", min_value=0.0, max_value=100.0, step=0.1)
button_clicked = st.button("Calculate Area and Perimeter")

if button_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"Area of the rectangle is: {area}")
    st.write(f"Perimeter of the rectangle is: {perimeter}")
