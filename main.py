import streamlit as st
import pandas as pd
import time

# Data Processing Optimization: Using Pandas built-in functions for faster computation
def process_data(data):
    # Perform data processing tasks here
    start_time = time.time()
    sum_column = data['Ticket ID'].sum()  # Example: Using pandas sum() function
    processing_time = round(time.time() - start_time, 2)
    return sum_column, processing_time

# Lazy Loading: Load and process data only when needed
@st.cache(show_spinner=False)
def load_and_process_data(file_path):
    data = pd.read_csv(file_path)
    sum_column, processing_time = process_data(data)
    return data, sum_column, processing_time

def main():
    st.title("Optimized Streamlit App")

    # Load and process data lazily when needed
    data, sum_column, processing_time = load_and_process_data('CGB_Consumer_Complaints_Data.csv')  # Replace 'your_dataset.csv' with your dataset file path
    st.write("Sum of 'Ticket ID' column:", sum_column)
    st.write("Processing time:", processing_time, "seconds")
    
    # Paging: Display data in chunks
    page_size = st.slider("Select page size:", min_value=1, max_value=len(data), value=10)
    current_page = st.number_input("Enter page number:", min_value=1, max_value=len(data) // page_size + 1, value=1)
    start_idx = (current_page - 1) * page_size
    end_idx = min(start_idx + page_size, len(data))
    st.write("Sample Data (Page {}):".format(current_page))
    st.write(data.iloc[start_idx:end_idx])

if __name__ == "__main__":
    main()
