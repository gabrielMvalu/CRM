import streamlit as st
from echarts import Echart, Legend, Line

# Initialize the main components
st.sidebar.header("Logo")
st.sidebar.button("Page 1")
st.sidebar.button("Page 2")
st.sidebar.button("Page 3")

st.sidebar.checkbox("Checkbox 01")
st.sidebar.checkbox("Checkbox 02")
st.sidebar.selectbox("ComboBox", options=["Option 1", "Option 2"])

 # Sidebar pentru încărcarea și afișarea logo-ului și textului
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

# Some placeholder text
st.text("Some interesting text goes here describing your app.")

# Chart placeholder
chart_placeholder = st.empty()

# Sample data for the chart
data = {
    'x': [0, 1, 2, 3, 4, 5],
    'y1': [5, 20, 36, 10, 10, 20],
    'y2': [15, 6, 45, 20, 35, 30]
}

# Create an Echart
chart = Echart('Chart_name', 'simple line chart')
chart.use(Line('y1', data['y1']))
chart.use(Line('y2', data['y2']))
chart.use(Legend(['y1', 'y2']))

# Display the chart
chart_placeholder.chart(chart, height="300px")

# Download button (you'll need to implement the data downloading logic)
st.download_button(label="Download Chart data", data="Your chart data here", file_name="chart_data.csv")
