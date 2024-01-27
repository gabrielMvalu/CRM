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
    edited_paragraphs = {f'para_{i}': {'text': para, 'edited': False, 'color': '🔴'} for i, para in enumerate(paragraphs)}

    for i, para in enumerate(paragraphs):
        with st.container():
            col1, col2, col3 = st.columns([1, 20, 1])
            with col1:
                st.markdown(edited_paragraphs[f'para_{i}']['color'], unsafe_allow_html=True)
            with col2:
                user_input = st.text_area(f"Paragraful {i+1}", value=para, key=f'para_{i}_input')
            with col3:
                if st.button('Salvează', key=f'save_{i}'):
                    if user_input != para:
                        edited_paragraphs[f'para_{i}']['color'] = '🔵'  # Modificat și diferit de original
                    else:
                        edited_paragraphs[f'para_{i}']['color'] = '🟢'  # Modificat dar identic cu originalul
                    edited_paragraphs[f'para_{i}']['text'] = user_input
                    edited_paragraphs[f'para_{i}']['edited'] = True

else:
    st.write("Vă rugăm să încărcați un document .docx în meniul din stânga.")
