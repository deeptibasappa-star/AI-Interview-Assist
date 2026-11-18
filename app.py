import streamlit as set
from groq import Groq
st.set_page_congif(page_title = "Placement Practice", layout = "centered")
st.title("AI Interview Assistant")
st.caption(" Practice and prepare for our Interview")
try:
  client = Groq(api_key = st.secrets("GROQ_API_KEY"))
  except(KeyError, FileNotFound):
    st.error("API Key is missing. Add it in Advanced Settings")
    st.stop()
    role = st.selectbox('Job Title', ['Machine learning engineer', 'senior software engineer','prompt engineer', 'data analyst', 'Devops engineer', 'other'])
