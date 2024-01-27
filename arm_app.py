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
    
    # Inițializează starea pentru fiecare paragraf dacă nu există deja în session_state
    for i, _ in enumerate(paragraphs):
        if f'para_{i}_state' not in st.session_state:
            st.session_state[f'para_{i}_state'] = '🔴'  # Stare inițială roșie
    
    for i, paragraph in enumerate(paragraphs):
        col1, col2 = st.columns([1, 20])
        with col1:
            # Afisează indicatorul pentru fiecare paragraf
            st.markdown(st.session_state[f'para_{i}_state'], unsafe_allow_html=True)
        with col2:
            # Folosește un key unic pentru fiecare text_area pentru a putea detecta modificările
            updated_text = st.text_area(f"Paragraful {i+1}", value=paragraph, height=100, key=f"para_{i}")
            if st.session_state[f'para_{i}'] != paragraph:
                st.session_state[f'para_{i}_state'] = '🔵'  # Schimbă în albastru dacă textul a fost modificat

else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
