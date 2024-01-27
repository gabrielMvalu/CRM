import streamlit as st
from PIL import Image
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from docx import Document



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

uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command1 = edited_df.loc[edited_df["rating"].idxmin()]["command"]
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

chart_data = pd.DataFrame(
   {"Variatia precipitatii per locatie": list(range(20)), favorite_command: np.random.randn(20), favorite_command1: np.random.randn(20)}
)

# Utilizați o diagramă cu bare grouped pentru a compara comanda favorită și "Balasan" pe fiecare locație
st.bar_chart(
    chart_data.set_index("Variatia precipitatii per locatie"),
    use_container_width=True
)

def docx_to_df(doc):
    tables = []
    for table in doc.tables:
        df = [['' for _ in range(len(table.columns))] for _ in range(len(table.rows))]
        for i, row in enumerate(table.rows):
            for j, cell in enumerate(row.cells):
                if cell.text:
                    df[i][j] = cell.text
        tables.append(pd.DataFrame(df))
    return tables

    if uploaded_file is not None:
        doc = Document(uploaded_file)
        tables = docx_to_df(doc)
        if tables:
            for i, table in enumerate(tables):
                st.write(f"Tabelul {i+1}")
                st.dataframe(table)
        else:
            st.write("Documentul nu conține tabele.")
    else:
        st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")

