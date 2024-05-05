import sys
import os
import streamlit as st

# Assuming all scripts are in the same directory as app.py
# directory_path = os.path.dirname(os.path.realpath(__file__))
# if directory_path not in sys.path:
#     sys.path.append(directory_path)
# from  dashboard import show_dashboard
from dashboard import show_dashboard
from home import show_home
from data_catalog import show_data_catalog
from api_access import show_api_access

with open('styles.css') as load_css:
    st.markdown(f'<style>{load_css.read()}</style>', unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a Page", ["Home", "Dashboard", "Data Catalog", "API Access"])

    if page == "Home":
        show_home()
    elif page == "Dashboard":
        show_dashboard()
    elif page == "Data Catalog":
        show_data_catalog()
    elif page == "API Access":
        show_api_access()

if __name__ == "__main__":
    main()
