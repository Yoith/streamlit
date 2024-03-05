import streamlit as st
import src.manage_data as cleaning

df = cleaning.load_dataframe()

st.write("Adventure time data")
st.dataframe(df)
