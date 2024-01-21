import streamlit as st
from PIL import Image
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sidebar for uploading and displaying logo and text
st.sidebar.title("CRM Predictii Oras Bailesti")

logo_path = "LogoSTR.PNG"

# Check if the file exists
if not os.path.exists(logo_path):
    st.sidebar.error("Logo file not found: " + logo_path)
else:
    try:
        logo = Image.open(logo_path)
        st.sidebar.image(logo, use_column_width=True)
    except IOError as e:
        st.sidebar.error("Error opening logo file: " + str(e))

st.sidebar.markdown("<small>© Castemill S.R.L.</small>", unsafe_allow_html=True)

# Sample dataframe
df = pd.DataFrame(
    {
        "command": ["st.selectbox", "st.balloons", "st.time_input"],
        "rating": [4, 5, 3],
        "is_widget": [True, False, True]
    }
)

# Display the dataframe
st.dataframe(df, num_rows="dynamic")
# Finding the command with the highest rating
favorite_command = df.loc[df["rating"].idxmax()]["command"]

st.markdown(f"Your favorite command is **{favorite_command}** 🎈")



chart_data = pd.DataFrame(
   {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
)

st.bar_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)
