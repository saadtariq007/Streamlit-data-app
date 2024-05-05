# dashboard.py
import streamlit as st
# from styles import load_css
import plotly.express as px
import pandas as pd
with open('styles.css') as load_css:
    st.markdown(f'<style>{load_css.read()}</style>', unsafe_allow_html=True)

def show_dashboard():
    # st.markdown(load_css(), unsafe_allow_html=True)
    st.title("Dashboard")
    cols = st.columns(4)
    metrics = [("Visitors", "30,794", "+22%"), ("Contacts", "1,983", "-21%"),
               ("Attributable Deals", "57.0", "-12.6%"), ("Revenue", "$10,622.21", "+15.2%")]

    for col, metric in zip(cols, metrics):
        col.metric(label=metric[0], value=metric[1], delta=metric[2])

    df = pd.DataFrame({
        'Month': ['January', 'February', 'March', 'April'],
        'Sales': [200, 250, 300, 350]
    })
    fig = px.line(df, x='Month', y='Sales', title='Monthly Sales')
    st.plotly_chart(fig, use_container_width=True)
