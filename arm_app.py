import streamlit as st


# Sidebar for uploading and displaying logo and text
st.sidebar.title("CRM predictii ors. Bailesti")
logo_path = "LogoSTR.PNG"
try:
    logo = Image.open(logo_path)
    st.sidebar.image(logo, use_column_width=True)
except IOError:
    st.sidebar.error("Eroare la încărcarea logo-ului.")
    st.sidebar.markdown("<small>© Castemill S.R.L.</small>", unsafe_allow_html=True)


