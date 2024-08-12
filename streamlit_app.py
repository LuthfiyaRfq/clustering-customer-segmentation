import streamlit as st
import pandas as pd
from src.model_loader import load_model
from src.cluster_result import explanation_result

model = load_model()

st.title("Clustering Customer Segmentation")

with st.form(key="form", clear_on_submit=True, border=True):
    st.subheader("Forms")

    income = st.number_input(key="income", label="How much do you earn?", step=1, min_value=0)
    st.write("")
    has_children = st.radio(key="kidhome", label="Do you have children?", options=["Yes", "No"])
    st.write("")
    has_teenage = st.radio(key="teenhome", label="Do you have teenage?", options=["Yes", "No"])
    st.write("")
    age = st.slider(key="age", label="Select Age", min_value=18, max_value=85)
    st.write("")
    has_partner = st.radio(key="partner", label="Do you have a partner?", options=["Yes", "No"])
    st.write("")
    education_level = st.radio(key="education", label="Select education", options=["Undergraduate", "Graduate", "Postgraduate"])
    
    st.divider()
    submit = st.form_submit_button(label="Submit")

container = st.container(border=True)
container.html("<h3>Input Results</h3>")

if submit:
    data = {
        'Income': [income],
        'Kidhome': [1 if has_children == "Yes" else 0],
        'Teenhome': [1 if has_teenage == "Yes" else 0],
        'Age': [age],
        'Partner': [has_partner],
        'Education_Level': [education_level]
    }
    new_data_df = pd.DataFrame(data)

    predicted_cluster = model.predict(new_data_df)

    data = {
        "Attribute": ["Income", "Has Children", "Has Teenage Children", "Age", "Has Partner", "Education Level", "Predicted Cluster"],
        "Value": [income, has_children, has_teenage, age, has_partner, education_level, predicted_cluster[0]]
    }
    df = pd.DataFrame(data)

    # Display the results
    container.table(df)
    explanation_result(predicted_cluster[0])
