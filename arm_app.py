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
    
    for i, original_text in enumerate(paragraphs):
        col1, col2, col3 = st.columns([1, 20, 1])
        with col1:
            # Inițializează indicatorul ca roșu pentru fiecare paragraf
            indicator_key = f'indicator_{i}'
            if indicator_key not in st.session_state:
                st.session_state[indicator_key] = '🔴'
            st.markdown(st.session_state[indicator_key], unsafe_allow_html=True)

        with col2:
            # Câmpul de text pentru editarea paragrafului, salvând textul editat în session_state
            text_key = f'text_{i}'
            user_input = st.text_area(f"Paragraful {i+1}", value=original_text if text_key not in st.session_state else st.session_state[text_key], key=text_key)

        with col3:
            # Butonul "Salvează" pentru fiecare paragraf
            if st.button('Salvează', key=f'save_{i}'):
                # Verifică dacă textul modificat este diferit de original
                if user_input != original_text:
                    st.session_state[indicator_key] = '🔵'  # Text modificat și diferit de original
                else:
                    st.session_state[indicator_key] = '🟢'  # Text modificat dar identic cu originalul
else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
