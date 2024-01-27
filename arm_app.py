import streamlit as st
from docx import Document

def read_docx(file):
    doc = Document(file)
    paragraphs = []
    for para in doc.paragraphs:
        paragraphs.append(para.text)
    return paragraphs

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

if uploaded_file is not None:
    paragraphs = read_docx(uploaded_file)
    updated_paragraphs = []
    for i, paragraph in enumerate(paragraphs):
        # Fiecare paragraf este afișat într-un câmp de text editabil
        updated_text = st.text_area(f"Paragraful {i+1}", value=paragraph, height=100)
        updated_paragraphs.append(updated_text)
    
    if st.button("Salvează Modificările"):
        # Aici poți adăuga logica pentru salvarea modificărilor, dacă este necesar
        st.success("Modificările au fost salvate!")
else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
