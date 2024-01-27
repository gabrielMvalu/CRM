import streamlit as st
from docx import Document
import os

def read_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

if uploaded_file is not None:
    text = read_docx(uploaded_file)
    st.write(text)
else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
