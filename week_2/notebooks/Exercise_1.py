# Exercise 1: Build a Data Explorer
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Explorer App")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Step 2: Load data
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Data")
    st.write(df.head())

   # Step 3: Show statistics
    st.subheader("Summary Statistics")
    st.write(df.describe(include="all"))

    # Step 4: Column filtering
    st.subheader("Filter Columns")
    selected_columns = st.multiselect(
        "Select columns to display",
        df.columns.tolist(),
        default=df.columns.tolist()
    )
    st.write(df[selected_columns].head())

    # Step 5: Auto visualization
    st.subheader("Automatic Visualizations")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        col_to_plot = st.selectbox("Choose a column for visualization", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[col_to_plot].dropna(), bins=30, color="skyblue", edgecolor="black")
        ax.set_title(f"Histogram of {col_to_plot}")
        st.pyplot(fig)
   else:
        st.info("No numeric columns available for visualization.")
