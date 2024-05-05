import streamlit as st

# Set page config
st.set_page_config(page_title='InsightStream', page_icon=':bar_chart:', layout='wide')

# Define a simple color palette
primary_color = "#0E1117"
secondary_color = "#FFFFFF"
accent_color = "#E694FF"

# Custom styles
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {primary_color};
    }}
    .css-18e3th9 {{
        background-color: {primary_color};
    }}
    .css-qbe2hs {{
        color: {secondary_color};
    }}
    h1, h2, h3, h4, h5, h6, .caption {{
        color: {accent_color};
    }}
    .stButton>button {{
        color: {secondary_color};
        background-color: {accent_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
st.title('InsightStream')
st.subheader('Empowering Data-Driven Decisions')

# Navigation bar (simple version using radio buttons)
app_section = st.sidebar.radio(
    "Navigate to:",
    ('Home', 'Financial Insights', 'Healthcare Quality', 'Demographic Insights', 'Geographic Mapping', 'Financial Markets')
)

# Content based on navigation choice
if app_section == 'Home':
    st.header('Welcome to InsightStream')
    st.write("Choose a section from the sidebar to start exploring valuable insights across different industries.")
    # st.image('path_to_welcome_image.jpg')  # Update path to your image file

elif app_section == 'Financial Insights':
    st.header('Financial Insights')
    st.write("Explore consumer financial behavior, trends, and more.")
    # Implement functionality here

elif app_section == 'Healthcare Quality':
    st.header('Healthcare Quality')
    st.write("Dive into hospital performance metrics and patient care quality across various regions.")
    # Implement functionality here

elif app_section == 'Demographic Insights':
    st.header('Demographic Insights')
    st.write("Analyze demographic data to uncover population trends and market potentials.")
    # Implement functionality here

elif app_section == 'Geographic Mapping':
    st.header('Geographic Mapping')
    st.write("Interact with our maps to get insights into geographical data points and more.")
    # Implement functionality here

elif app_section == 'Financial Markets':
    st.header('Financial Markets')
    st.write("Get the latest trends and analytics from the financial sector.")
    # Implement functionality here

# Footer
st.markdown('---')
st.text('InsightStream © 2024 | All rights reserved')
st.text('Follow us on [Twitter](https://twitter.com/yourtwitterhandle) | [LinkedIn](https://linkedin.com/company/yourcompany)')
