import streamlit as st
import pandas as pd

st.title("Sales Data Analysis")

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Sales": [80000, 50000, 30000, 75000, 55000]
}

df = pd.DataFrame(data)

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Total Sales")
st.write(df["Sales"].sum())

st.subheader("Highest Sales")
st.write(df["Sales"].max())

st.subheader("Lowest Sales")
st.write(df["Sales"].min())

st.subheader("Sales Chart")
st.bar_chart(df.set_index("Product")["Sales"])