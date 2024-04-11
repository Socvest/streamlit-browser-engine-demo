import streamlit as st
from browser_engine import browser_detection_engine

st.set_page_config(layout="wide")
value = browser_detection_engine(singleRun=False)
st.write(value) 
