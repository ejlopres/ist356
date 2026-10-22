import streamlit as st

from figures import df1, df2, df3, df4, df5, df6, df7, df8

grade = st.text_input("Enter your grade (A, B, C, D, F):")
message = ""
if grade == "A":
    message = "Excellent work!"


st.dataframe(df1)
st.dataframe(df2)
st.dataframe(df3)
st.dataframe(df4)
st.dataframe(df5)
st.dataframe(df6)
st.dataframe(df7)
st.dataframe(df8)

