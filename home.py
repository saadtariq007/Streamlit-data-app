# home.py
import streamlit as st
# from styles import load_css
with open('styles.css') as load_css:
    st.markdown(f'<style>{load_css.read()}</style>', unsafe_allow_html=True)

def show_home():
    # st.markdown(load_css(), unsafe_allow_html=True)
    st.title("Welcome to UnifyData Dashboard")
    st.write("Empowering Data-Driven Decisions with Real-Time Insights")
    
    st.header("Key Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Comprehensive Data Catalog')
    with col2:
        st.subheader("Real-Time Analytics")
        st.write("Access up-to-the-minute data visualizations and analytics.")
    with col3:
        st.subheader("API Access")
        st.write("Seamlessly integrate with our robust data APIs.")

    if st.button("Explore Data"):
        st.experimental_rerun()  # Re-run to simulate navigation

    st.header("What Our Users Say")
    st.info("“This platform has transformed the way we approach market analysis. The real-time data insights are invaluable.” - Jane Doe, Data Analyst")
