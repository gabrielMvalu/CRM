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
st.dataframe(df)

# Create a bar chart based on the dataframe
fig, ax = plt.subplots()
df.plot(kind='bar', x='command', y='rating', ax=ax)
ax.set_xlabel('Command')
ax.set_ylabel('Rating')
st.pyplot(fig)

# Finding the command with the highest rating
favorite_command = df.loc[df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
