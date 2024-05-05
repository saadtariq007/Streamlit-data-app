# api_access.py
import streamlit as st
with open('styles.css') as load_css:
    st.markdown(f'<style>{load_css.read()}</style>', unsafe_allow_html=True)
def show_api_access():
    # st.markdown(load_css(), unsafe_allow_html=True)
    st.subheader("API Access")
    st.write("Learn how to integrate our data into your applications.")
