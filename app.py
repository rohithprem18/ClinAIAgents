import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv  
from agent_logic import generate_csr_narrative

load_dotenv() 

st.set_page_config(page_title="ClinAIAgent Demo", page_icon="💊", layout="wide")

st.title("ClinAIAgent Prototype 💊")
st.write("Running locally on your machine!")

# Read the API key from the environment variable (loaded from .env)
gemini_api_key = os.getenv("GOOGLE_API_KEY" )

with st.sidebar:
    st.header("Control Panel")
    if not gemini_api_key:
        st.warning("API Key not found! Create a .env file.", icon="⚠️")

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    use_sample_data = st.button("Or use sample data")

if 'df' not in st.session_state:
    st.session_state.df = None

if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file)
elif use_sample_data:
    csv_data = '''patient_id,treatment_group,age,adverse_event
P001,DrugA,45,Headache
P002,DrugA,52,Nausea
P003,Placebo,48,Headache
P004,DrugA,60,Headache
P005,Placebo,55,None
P006,Placebo,62,Nausea'''
    st.session_state.df = pd.read_csv(pd.io.common.StringIO(csv_data))

if st.session_state.df is None:
    st.info("Upload a CSV or load sample data to start.", icon="👈")
else:
    st.subheader("Data Preview")
    st.dataframe(st.session_state.df)

    if st.button("✨ Generate Narrative", type="primary"):
        if not gemini_api_key:
            st.error("API Key not found. Make sure it's in your .env file.", icon="🚨")
        else:
            with st.spinner("Agent is working..."):
                narrative = generate_csr_narrative(st.session_state.df, gemini_api_key)
            st.subheader("📝 Generated Narrative")
            st.markdown(f"> {narrative}")
            st.toast('Narrative generated!', icon='🎉')
