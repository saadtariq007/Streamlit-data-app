# data_catalog.py
import streamlit as st
import pandas as pd
# from styles import load_css
with open('styles.css') as load_css:
    st.markdown(f'<style>{load_css.read()}</style>', unsafe_allow_html=True)
def show_data_catalog():
    # st.markdown(load_css(), unsafe_allow_html=True)
    st.subheader("Data Catalog")
    st.write("Here, users can search and explore various datasets.")
    st.subheader("Comprehensive Data Catalog")
    st.write("Explore a vast array of datasets tailored for various industries.")
    df = create_data_catalog()

    source_filter = st.sidebar.multiselect('Filter by Source:', options=df['Source'].unique(), default=df['Source'].unique())
    filtered_data = df[df['Source'].isin(source_filter)]

    st.dataframe(filtered_data)  # Display the data in the app

def create_data_catalog():
    data = {
        'Dataset Name': [
            'AccessGUDID', 'ACS (American Community Survey)', 'Social Capital Atlas', 
            'Severe Weather Data Inventory', 'AirData', 'Darthmouth Atlas', 'Open Payments', 
            'FEC Campaign Finance', 'US Inflation and Unemployment'
        ],
        'Source': [
            'FDA', 'U.S. Census Bureau', 'Social Capital Project', 
            'NOAA', 'EPA', 'Darthmouth College', 'CMS', 
            'Federal Election Commission', 'U.S. Bureau of Labor Statistics'
        ],
        'Description': [
            'Unique device identifiers (UDI) database to adequately identify devices through distribution and use.',
            'Surveys data from the U.S. communities, providing current data on the social and economic conditions of the U.S.',
            'Interactive data and maps on the social capital variables in different regions.',
            'Data related to severe weather conditions to aid in risk assessment and research.',
            'Air quality data from across the US, including pollutants and health advisories.',
            'Health and demographic data to provide comprehensive information on health care and outcomes.',
            'Database of payments made by health care companies to physicians and teaching hospitals.',
            'Campaign finance data from 1980 to the present, including detailed financial reports.',
            'Economic statistics for inflation, prices, and unemployment rates in the U.S.'
        ]
    }
    return pd.DataFrame(data)
