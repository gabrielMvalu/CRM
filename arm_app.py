import streamlit as st
from docx import Document
import pandas as pd

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

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

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
