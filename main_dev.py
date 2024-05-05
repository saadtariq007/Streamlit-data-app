import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Define a function to load CSS for styling
def load_css():
    """Load custom CSS for the Streamlit app, applying the 'Calm and Technical' color palette."""
    css = """
    <style>
        /* Main text and headers color - Slate Grey */
        body, h1, h2, h3, h4, h5, h6, .stButton > button {
            color: #596E79;
        }
        
        /* Primary background color - Light Blue Grey */
        body, .stApp, .stTextInput > input {
            background-color: #ECEFF1;
        }
        
        /* Sidebar background - Grey */
        .css-1lcbmhc {
            background-color: #B2B2B2;
        }
        
        /* Accent color for buttons and active elements - Green */
        .stButton > button, .stTextInput > input:focus {
            background-color: #4CAF50;
            border-color: #4CAF50;
        }
        
        /* Hover effect for buttons */
        .stButton > button:hover {
            background-color: #367c39;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
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
# Home Page Layout
def create_home_page():
    st.title("Welcome to UnifyData Dashboard")
    st.write("Empowering Data-Driven Decisions with Real-Time Insights")

    # Feature Highlights
    st.header("Key Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        # st.image("icon1.png")  # Assuming icons are stored locally
        st.header('ss')
    with col2:
        # st.image("icon2.png")
        st.subheader("Real-Time Analytics")
        st.write("Access up-to-the-minute data visualizations and analytics.")
    with col3:
        # st.image("icon3.png")
        st.subheader("API Access")
        st.write("Seamlessly integrate with our robust data APIs.")

    # Call to Action
    if st.button("Explore Data"):
        st.experimental_rerun()  # Re-run to simulate navigation to the data catalog page

    # Testimonials
    st.header("What Our Users Say")
    st.info("“This platform has transformed the way we approach market analysis. The real-time data insights are invaluable.” - Jane Doe, Data Analyst")

# Main Function: Layout and Navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a Page", ["Home", "Dashboard", "Data Catalog", "API Access"])

    if page == "Home":
        create_home_page()
    elif page == "Dashboard":
        create_dashboard()
    elif page == "Data Catalog":
        st.subheader("Data Catalog")
        st.write("Here, users can search and explore various datasets.")
        st.subheader("Comprehensive Data Catalog")
        st.write("Explore a vast array of datasets tailored for various industries.")
        df = create_data_catalog()

    # Filtering options
        source_filter = st.sidebar.multiselect('Filter by Source:', options=df['Source'].unique(), default=df['Source'].unique())
        filtered_data = df[df['Source'].isin(source_filter)]

        st.dataframe(filtered_data)  # Display the data in the app
    elif page == "API Access":
        st.subheader("API Access")
        st.write("Learn how to integrate our data into your applications.")

# Define the Dashboard Page
def create_dashboard():
    st.title("Dashboard")
    cols = st.columns(4)
    metrics = [("Visitors", "30,794", "+22%"), ("Contacts", "1,983", "-21%"),
               ("Attributable Deals", "57.0", "-12.6%"), ("Revenue", "$10,622.21", "+15.2%")]

    for col, metric in zip(cols, metrics):
        col.metric(label=metric[0], value=metric[1], delta=metric[2])

    with st.container():
        # Example data for plotting
        df = pd.DataFrame({
            'Month': ['January', 'February', 'March', 'April'],
            'Sales': [200, 250, 300, 350]
        })
        fig = px.line(df, x='Month', y='Sales', title='Monthly Sales')
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
