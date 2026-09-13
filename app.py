import streamlit as st
import pandas as pd

st.title("Student Marks Analysis")

# Student data
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Marks": [85, 72, 91, 65, 78]
}

df = pd.DataFrame(data)

st.subheader("Student Data")
st.dataframe(df)

# Analysis
average = df["Marks"].mean()
highest = df["Marks"].max()
lowest = df["Marks"].min()

st.subheader(" Analysis")

st.write("Average Marks:", round(average, 2))
st.write("Highest Marks:", highest)
st.write("Lowest Marks:", lowest)

st.subheader("Marks Chart")
st.bar_chart(df.set_index("Name"))