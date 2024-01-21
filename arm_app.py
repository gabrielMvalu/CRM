import streamlit as st
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Line
from pyecharts import options as opts
from PIL import Image

# Sidebar for uploading and displaying logo and text
st.sidebar.title("CRM predictii ors. Bailesti")
logo_path = "LogoSTR.PNG"
try:
    logo = Image.open(logo_path)
    st.sidebar.image(logo, use_column_width=True)
except IOError:
    st.sidebar.error("Eroare la încărcarea logo-ului.")
    st.sidebar.markdown("<small>© Castemill S.R.L.</small>", unsafe_allow_html=True)

# Main panel with the app name and chart
st.header("My_app_name")
st.text("Some interesting text goes here describing your app.")

# Sample data for the chart
x_data = [0, 1, 2, 3, 4, 5]
y1_data = [5, 20, 36, 10, 10, 20]
y2_data = [15, 6, 45, 20, 35, 30]

# Create an Echart line chart
line_chart = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("Series 1", y1_data)
    .add_yaxis("Series 2", y2_data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Chart_name"))
)

# Display the chart using Streamlit Echarts
st_pyecharts(line_chart)

# Data for download (example using CSV format)
csv = 'Time,Series 1,Series 2\n'
csv += '\n'.join([f"{x},{y1},{y2}" for x, y1, y2 in zip(x_data, y1_data, y2_data)])

st.download_button(label="Download Chart data", data=csv, file_name="chart_data.csv", mime='text/csv')
