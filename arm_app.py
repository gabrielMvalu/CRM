import streamlit as st
from docx import Document
import pandas as pd

def extract_text_and_tables(doc):
    elements = []  # Lista care va conține textul și tabelele

    # Extragerea textului
    for para in doc.paragraphs:
        if para.text:  # Dacă paragraful conține text, adaugă-l la listă
            elements.append({'type': 'text', 'content': para.text})

    # Extragerea tabelelor
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)
        df = pd.DataFrame(table_data)
        elements.append({'type': 'table', 'content': df})

    return elements

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

if uploaded_file is not None:
    doc = Document(uploaded_file)
    elements = extract_text_and_tables(doc)
    
    for element in elements:
        if element['type'] == 'text':
            st.write(element['content'])
        elif element['type'] == 'table':
            st.dataframe(element['content'])
else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
