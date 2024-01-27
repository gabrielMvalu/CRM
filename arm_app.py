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
    
    for i, original_text in enumerate(paragraphs):
        key = f'para_{i}'
        edited_key = f'edited_{i}'

        # Inițializează starea pentru fiecare paragraf dacă nu există deja în session_state
        if key not in st.session_state:
            st.session_state[key] = original_text  # Salvează textul original
            st.session_state[edited_key] = False  # Marchează paragraful ca needitat inițial
        
        col1, col2 = st.columns([1, 20])
        with col1:
            if st.session_state[edited_key]:  # Dacă paragraful a fost editat
                color = '🔵' if st.session_state[key] != original_text else '🟢'
            else:
                color = '🔴'
            st.markdown(color, unsafe_allow_html=True)
        
        with col2:
            # Utilizatorul editează textul
            user_input = st.text_area(f"Paragraful {i+1}", value=st.session_state[key], height=100, key=key)
            
            # Verifică dacă textul a fost modificat și actualizează starea
            if user_input != st.session_state[key]:
                st.session_state[edited_key] = True  # Marchează ca editat
                st.session_state[key] = user_input  # Actualizează textul salvat cu cel modificat

else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
