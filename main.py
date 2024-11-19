

import streamlit as st
import pandas as pd

# Add custom CSS styles
st.markdown(
    """
    <style>
    /* Sidebar customization */
    [data-testid="stSidebar"] {
        background-color: #f7f7f7;
        border-right: 1px solid #ddd;
    }

    /* Main title */
    h1 {
        color: #1f77b4;
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Secondary headings */
    h2, h3 {
        color: #333;
        font-family: 'Arial', sans-serif;
    }

    /* Data table */
    .dataframe {
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    /* Filter text */
    .stSelectbox label {
        font-weight: bold;
        color: #444;
    }

    /* Button customization */
    button {
        background-color: #1f77b4 !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
        font-size: 14px !important;
    }

    /* Add space between sections */
    section {
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add the image at the top
st.image("foot.jpeg", use_container_width=True, caption="Football player data")

# Application title
st.title("Football Player Data Exploration")

# Load the data
file_name = "f.csv"  # Name of your CSV file
try:
    data = pd.read_csv(file_name)

    # Display raw data
    st.header("Raw Data")
    st.dataframe(data)

    # Filter options
    st.sidebar.header("Filters")
    position = st.sidebar.selectbox(
        "Field Position",
        options=["All"] + data["position_field"].dropna().unique().tolist()
    )
    country = st.sidebar.selectbox(
        "Country of Birth",
        options=["All"] + data["country_birth"].dropna().unique().tolist()
    )

    # Apply filters
    filtered_data = data.copy()
    if position != "All":
        filtered_data = filtered_data[filtered_data["position_field"] == position]
    if country != "All":
        filtered_data = filtered_data[filtered_data["country_birth"] == country]

    # Display filtered data
    st.header("Filtered Data")
    st.write(f"Number of results: {len(filtered_data)}")
    st.dataframe(filtered_data)

    # Height and weight statistics
    if "height" in data.columns and "weight" in data.columns:
        st.header("Player Statistics")
        st.write("Height statistics (cm):")
        st.write(filtered_data["height"].describe())
        st.write("Weight statistics (kg):")
        st.write(filtered_data["weight"].describe())
except FileNotFoundError:
    st.error(f"The file {file_name} could not be found. Please check the path.")
