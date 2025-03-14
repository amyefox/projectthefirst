import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/amyefox/projectthefirst/main/Employee%20groups%20and%20classes.csv")
    return df.groupby("Employee Group")["Required Class"].apply(set).to_dict()

# Load data
role_class_mapping = load_data()

# Streamlit App Layout
st.title("Class Requirement Finder")

# Multi-select dropdown for employee roles
selected_roles = st.multiselect("Select Your Roles:", options=sorted(role_class_mapping.keys()))

# Find required classes for selected roles
required_classes = set()
for role in selected_roles:
    required_classes.update(role_class_mapping.get(role, []))

# Display results
st.subheader("Required Classes:")
if required_classes:
    for course in sorted(required_classes):
        st.write(f"✅ {course}")
else:
    st.write("No classes required.")
