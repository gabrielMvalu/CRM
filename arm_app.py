
import streamlit as st
from docx import Document
import pandas as pd
import numpy as np
import pydeck as pdk


st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

      def read_docx(file):
            doc = Document(file)
            paragraphs = [para.text for para in doc.paragraphs if para.text.strip() != '']
            return paragraphs
  

  
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

  
col1, col2 = st.columns(2)
with col1:
  chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

  st.vega_lite_chart(
     chart_data,
      {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
      "config": {"view": {"stroke": ""}},
      "width": 600,
      "height": 200,
      "data": {
        "values": [
          {"country": "PSD", "animal": "porci"},
          {"country": "PSD", "animal": "porci"},
          {"country": "PSD", "animal": "vaci"},
          {"country": "PSD", "animal": "vaci"},
          {"country": "PSD", "animal": "vaci"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "PSD", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "porci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "vaci"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"},
          {"country": "Restul Partidelor", "animal": "oi"}
        ]
      },
      "transform": [
        {
          "calculate": "{'vaci': '🐄', 'porci': '🐖', 'oi': '🐏'}[datum.animal]",
          "as": "emoji"
        },
        {"window": [{"op": "rank", "as": "rank"}], "groupby": ["country", "animal"]}
      ],
      "mark": {"type": "text", "baseline": "middle"},
      "encoding": {
        "x": {"field": "rank", "type": "ordinal"},
        "y": {"field": "animal", "type": "nominal"},
        "row": {"field": "country", "header": {"title": ""}},
        "text": {"field": "emoji", "type": "nominal"},
        "size": {"value": 65}
      }
    }
  )

with col2:
  st.write("Tzanca #1")
  
  
