import streamlit as st


st.set_page_config(page_title="Survey of Conusmer Finances 2022",layout="wide",initial_sidebar_state="expanded")
st.title("Analysis of Survey of Consumer Finances 2022 Data")

st.write("### This data was collected from {https://www.federalreserve.gov/econres/scfindex.htm}")

import pandas as pd
import plotly.express as px

df_2022 = pd.read_csv("Dataset/SCFP2022.csv")

st.write("### The sample data from 2022 looks like this:")
st.dataframe(df_2022.head())
url = "https://sda.berkeley.edu/sdaweb/docs/scfcomb2022/DOC/hcbkh01.htm"
st.write(f"For more information related to Data Dictionary visit the url {url}")

st.write("### The total dataset has {} rows and {} columns.".format(df_2022.shape[0], df_2022.shape[1]))



df_2022['RACE'] = df_2022['RACE'].replace({1: 'White non-Hispanic', 2: 'Black/African American', 
                                           3: 'Hispanic', 4: 'Asian', 5: 'Other'})
# Convert the 'race' column to categorical data type
df_2022['RACE'] = df_2022['RACE'].astype('category')
race_counts = df_2022['RACE'].value_counts()

# Plot the bar chart
fig = px.bar(x=race_counts.index, y=race_counts.values, labels={'x': 'Race', 'y': 'Count'}, 
             title=' Bar Chart of Race'
            )
fig.update_layout(height = 500, width = 700)

st.write(fig)

