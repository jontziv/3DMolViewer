import streamlit as st

st.set_page_config(page_title="MolViewer", page_icon="🧬",layout="wide",initial_sidebar_state="auto")
st.sidebar.markdown('''
    https://github.com/jontziv/3DMolViewer
    ''')  
with open(f'README.md', 'r') as f:           
    st.markdown(f.read(),unsafe_allow_html=True)
                                                                    

                    


