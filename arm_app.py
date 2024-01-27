import streamlit as st
from docx import Document

def read_docx(file):
    doc = Document(file)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip() != '']
    return paragraphs

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

if uploaded_file is not None:
    paragraphs = read_docx(uploaded_file)
    
    for i, para in enumerate(paragraphs):
        col1, col2, col3 = st.columns([1, 20, 1])
        with col1:
            # Inițializează indicatorul ca roșu pentru fiecare paragraf
            if f'color_{i}' not in st.session_state:
                st.session_state[f'color_{i}'] = '🔴'
            st.markdown(st.session_state[f'color_{i}'], unsafe_allow_html=True)
        with col2:
            # Câmpul de text pentru editarea paragrafului
            user_input = st.text_area(f"Paragraful {i+1}", value=para, key=f'text_{i}')
        with col3:
            # Butonul "Salvează" pentru fiecare paragraf
            if st.button('Salvează', key=f'save_{i}'):
                # Schimbă culoarea în albastru după salvare
                st.session_state[f'color_{i}'] = '🔵'
else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
