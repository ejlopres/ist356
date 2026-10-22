# Let's build an interactive pivot table in streamlit!

# - create a row and column selection widgets allowing the user to select one of the following columns:  
# `'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
# - create a measure column selestion widget which allows the user to select one of these columns:  
# `'Completion_Time','Student_Score'`
# - build the pivot table dataframe from the inputs. use the average for the `aggfunc`
# - display the pivot table!

# **EXTRA CHALLENGE:** Do not allow the name value in row and column!



import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.write(list(exams.columns))
st.dataframe(exams)

row = "Exam_Version"
col = "Studied_In_Groups"
measure = "Completion_Time"

st.title("Interactive Pivot Table")

#inputs
row_col_values = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measure_values = ['Completion_Time','Student_Score']

row = st.selectbox("Select Row", row_col_values)
col = st.selectbox("Select Column", row_col_values)
measure = st.selectbox("Select Measure", measure_values)

#process
try:
    if row == col:
        st.error("Row and Column cannot be the same. Please select different values.")
    else:
        pivot1 = exams.pivot_table(index=row, columns=col, values=measure, aggfunc='mean')

        #output
        st.write(f"Pivote table: '{row}' x '{col}' with '{measure}' as mean")
        st.dataframe(pivot1)
except Exception as e:
    st.error(f"An error occurred while creating the pivot table: {e}")



#output
st.write(f"Pivote table: '{row}' x '{col}' with '{measure}' as mean")
st.dataframe(pivot1)