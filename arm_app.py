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

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")



chart_data = pd.DataFrame(
   {"Bailesti": list(range(20)), "Seaca": np.random.randn(20), "Balasan": np.random.randn(20)}
)

st.bar_chart(
   chart_data, x="Bailesti", y=["Seaca", "Balasan"], color=["#6fa8dc", "#7a5fcc"]  # Optional
)
