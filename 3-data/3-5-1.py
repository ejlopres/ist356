import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.write(list(exams.columns))
st.dataframe(exams)

exams_by_section = exams.groupby(by=['Class_Section']).agg({ 'Class_Section': 'count', 'Student_Score': 'mean' })
st.dataframe(exams_by_section)

exam_counts_by_section_and_version = exams.groupby(by=['Class_Section', 'Exam_Version']).agg({ 'Class_Section': 'count', 'Student_Score': 'mean' })
st.dataframe(exam_counts_by_section_and_version)




#group by did exam prep assignment, and we want t count students and get the mean of their student score.
df2 = exams.groupby(by=['Did_Exam_Prep Assignment']).agg({ 'Exam_Version': 'count', 'Student_Score': 'mean' })
df2 = df2.rename(columns={'Exam_Version': 'Student Count', 'Student_Score': 'Mean Score'})
st.dataframe(df2)

st.header("Pivot and Melt")

# Get average scores by section and exam version:
avg_scores_by_section_and_version = exams.groupby(by=['Class_Section', 'Exam_Version']).agg({'Student_Score': 'mean'})

# add section and exam version back to dataframe
avg_scores_by_section_and_version['Class_Section'] = avg_scores_by_section_and_version.index.get_level_values('Class_Section')
avg_scores_by_section_and_version['Exam_Version'] = avg_scores_by_section_and_version.index.get_level_values('Exam_Version')
# reset the index
avg_scores_by_section_and_version = avg_scores_by_section_and_version.reset_index(drop=True)
#rename the Student_score to average score
avg_scores_by_section_and_version =  avg_scores_by_section_and_version.rename(columns={'Student_Score': 'Average_Score'})
#reorder the columns
avg_scores_by_section_and_version = avg_scores_by_section_and_version[['Class_Section', 'Exam_Version', 'Average_Score']]

#show
st.dataframe(avg_scores_by_section_and_version)

#pivot
pivot1 = avg_scores_by_section_and_version.pivot(index='Class_Section', columns='Exam_Version', values='Average_Score')
st.dataframe(pivot1)    

melted1 = pivot1.reset_index().melt(id_vars='Class_Section', value_name='Average_Score', var_name='Exam_Version')
st.dataframe(melted1)

#pivot table exams in row Class_Section, in Columns Exam_Version, values Student_Score, aggfunc mean
pivot_table1 = pd.pivot_table(exams, index='Class_Section', columns='Exam_Version', values='Student_Score', aggfunc='mean')
st.dataframe(pivot_table1)