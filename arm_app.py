
import streamlit as st
from docx import Document
import pandas as pd
import numpy as np
import pydeck as pdk

import React from 'react';
import { FloatButton } from 'antd';

const App: React.FC = () => <FloatButton onClick={() => console.log('onClick')} />;

export default App;


st.sidebar.title("Încărcare Document")
uploaded_file = st.sidebar.file_uploader("Alege un fișier .docx", type="docx")

        
tab1, tab2 = st.tabs(["PARTidisti", "Manelisti"])
with tab1:
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

with tab2:
  st.write("Tzanca Urangutanu este #1")
  
  
