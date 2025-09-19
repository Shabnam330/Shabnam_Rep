# Exercise 2: Machine Learning App
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.title("🤖 Machine Learning App")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Data")
    st.write(df.head())

    # Step 2: Select features and target
    st.subheader("Select Features and Target")
    all_columns = df.columns.tolist()
    target_col = st.selectbox("Select target column", all_columns)
    feature_cols = st.multiselect("Select feature columns", [c for c in all_columns if c != target_col])

    if feature_cols and target_col:
        X = df[feature_cols]
        y = df[target_col]

        # Step 3: Train/Test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Step 4: Train model
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Step 5: Evaluate model
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        st.subheader("📈 Model Metrics")
        st.write(f"Accuracy: **{acc:.2f}**")
        st.text("Classification Report:")
        st.text(classification_report(y_test, y_pred))

        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)

        # Step 6: Predict new data
        st.subheader("🔮 Make Predictions")
        input_data = {}
        for col in feature_cols:
            val = st.number_input(f"Enter value for {col}", float(df[col].min()), float(df[col].max()),   float(df[col].mean()))
            input_data[col] = val
        if st.button("Predict"):
            new_df = pd.DataFrame([input_data])
            prediction = model.predict(new_df)[0]
            st.success(f"Predicted class: **{prediction}**")