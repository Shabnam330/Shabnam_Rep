# Exercise 3 
multipage_app/
│
├── Home.py
├── pages/
│   ├── 1_Data_Analysis.py
│   └── 2_Settings.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Multi-Page Dashboard", layout="wide")

st.title("🏠 Home Page - KPIs")

# Example dataset
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "sales": [100, 200, 300, 400, 500],
        "profit": [20, 50, 80, 70, 120],
        "region": ["North", "South", "East", "West", "Central"]
    })

df = st.session_state.data
# KPIs
st.metric("Total Sales", f"${df['sales'].sum():,}")
st.metric("Total Profit", f"${df['profit'].sum():,}")
st.metric("Average Profit Margin", f"{(df['profit'].sum()/df['sales'].sum()):.2%}")

st.info("Use the sidebar to navigate to other pages.")

import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Data Analysis")

df = st.session_state.data

# Bar chart
st.subheader("Sales by Region")
fig, ax = plt.subplots()
ax.bar(df["region"], df["sales"], color="skyblue")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Scatter plot
st.subheader("Profit vs Sales")
fig, ax = plt.subplots()
ax.scatter(df["sales"], df["profit"], color="green")
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
st.pyplot(fig)

import streamlit as st
import pandas as pd

st.title("⚙️ Settings / Configuration")

# Example: change dataset values
new_sales = st.number_input("Set base sales value", min_value=50, max_value=1000, value=100)

if st.button("Apply Changes"):
    df = st.session_state.data.copy()
    df["sales"] = df["sales"] + new_sales
    st.session_state.data = df
    st.success("Dataset updated! Go back to Home or Data Analysis to see changes.")



