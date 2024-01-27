
import streamlit as st
from docx import Document

def read_docx(file):
    doc = Document(file)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip() != '']
    return paragraphs

st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

if uploaded_file is not None:
    # Încarcă și prelucrează documentul o singură dată
    if 'paragraphs' not in st.session_state or st.session_state.uploaded_file != uploaded_file:
        st.session_state.paragraphs = read_docx(uploaded_file)
        st.session_state.paragraph_states = ['🔴' for _ in st.session_state.paragraphs]  # Inițializează toți indicatorii ca roșii
        st.session_state.uploaded_file = uploaded_file

    for i, original_text in enumerate(st.session_state.paragraphs):
        col1, col2, col3 = st.columns([1, 20, 5])
        with col1:
            st.markdown(st.session_state.paragraph_states[i], unsafe_allow_html=True)
        with col2:
            # Folosește un key unic pentru fiecare text_area pentru a putea detecta modificările
            user_input = st.text_area(f"Paragraful {i+1}", value=original_text, key=f'para_{i}')
        with col3:
            save_button = st.button('Salvează', key=f'save_{i}')
            if save_button:
                if user_input != original_text:
                    st.session_state.paragraph_states[i] = '🔵'  # Modificat și diferit de original
                else:
                    st.session_state.paragraph_states[i] = '🟢'  # Modificat dar identic cu originalul
                st.experimental_rerun()

else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
