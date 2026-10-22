import streamlit as st
import pandas as pd
import datetime



base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/"
roster = pd.read_csv(base + "roster.csv")

start_date = datetime.date(2024, 1, 8)
class_split = datetime.timedelta(days=7)
end_date = datetime.date(2024, 5, 24)

polls = []
for i in range(4):
    file_date = start_date + i * class_split
    file_date_string = datetime.datetime.strftime(file_date, "%Y-%m-%d")
    filename = f"poll-responses-{file_date_string}.csv"
    st.write(f"importing {filename}")
    poll = pd.read_csv(base + filename)
    poll['poll_date'] = file_date
    poll['poll_filename'] = filename
    polls.append(poll)

polls_concat = pd.concat(polls, ignore_index=True)

# merge the roster with the polls_concat dataframe
polls_merged = pd.merge(roster, polls_concat, how='left', left_on="netid", right_on='student_id')

# use pivot table so roster data is in the row and the poll_date values are in the columns and the values are the count of the poll responses
polls_pivot = pd.pivot_table(polls_merged, index=['netid', 'name'], columns='poll_date', values='answer', aggfunc='count', fill_value=0)

# now melt the pibot table so that the poll_date is a column instead of an index
polls_melted = polls_pivot.reset_index().melt(id_vars=['netid', 'name'], var_name='poll_date', value_name='response_count')


# student in row, count of responses bigger than zero in column
students_with_reponses = polls_melted[polls_melted['response_count'] > 0].groupby(['netid', 'name']).size().reset_index(name='num_responses')

st.dataframe(roster)
st.dataframe(polls_concat)
st.dataframe(polls_merged)
st.dataframe(polls_pivot)
st.dataframe(polls_melted)
st.dataframe(students_with_reponses)