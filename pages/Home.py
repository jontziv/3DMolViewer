from streamlit_navigation_bar import st_navbar
import streamlit as st
import streamlit as st
import py3Dmol
import requests
import biotite.structure.io as bsio
from stmol import *

st.set_page_config(page_title="Stmol", page_icon="🧬",layout="wide",initial_sidebar_state="auto")
st.sidebar.markdown('''
    Placeholder
    ''')  
with open(f'README.md', 'r') as f:           
    st.markdown(f.read(),unsafe_allow_html=True)



