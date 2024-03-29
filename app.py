import streamlit as st
from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas as pd

# from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv
import os

if os.path.exists("./dataset.csv"):
    df = pd.read_csv("dataset.csv", index_col=None)

with st.sidebar:
    st.image("img.jpeg")
    st.title("AutoML")
    choice = st.radio("Navigation", ["Upload", "Profiling", "Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset for regression")
    file = st.file_uploader("Upload Your Dataset")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("dataset.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Exploratory Data Analysis")
    if st.button("View EDA Report"):
        report = sv.analyze(df)
        report.show_html()


if choice == "Modelling":
    chosen_target = st.selectbox("Choose the Target Column", df.columns)
    if st.button("Run Modelling"):
        setup(
            df, target=chosen_target, verbose=False
        )  # Adjusted to set verbose=False instead of silent=True
        setup_df = pull()
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, "best_model")


if choice == "Download":
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download Model", f, file_name="best_model.pkl")
    with open("Run.ipynb", "rb") as f:
        st.download_button("Load Model File", f, file_name="Run.ipynb")
