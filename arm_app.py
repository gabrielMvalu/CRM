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
    original_paragraphs = paragraphs.copy()
    states = ['🔴' for _ in paragraphs]  # Inițializează toți indicatorii ca roșii

    for i, paragraph in enumerate(paragraphs):
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown(states[i], unsafe_allow_html=True)
        with col2:
            updated_text = st.text_area(f"Paragraful {i+1}", value=paragraph, height=100, key=f"para_{i}")
        
        if updated_text != original_paragraphs[i]:
            states[i] = '🔵'  # Schimbă indicatorul în albastru dacă textul a fost modificat
        if st.session_state.get(f"para_{i}"):
            states[i] = '🟢'  # Schimbă indicatorul în verde dacă paragraful este selectat pentru modificare

else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
