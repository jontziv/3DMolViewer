import streamlit as st
import py3Dmol
from stmol import showmol
import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import biotite.structure.io as bsio
import stmol
import py3Dmol
import glob 
from st_speckmol import speck_plot 
from stmol import showmol,render_pdb,render_pdb_resn
import os

st.sidebar.markdown('''
    

    ''')  
### Step 2) Streamlit

st.sidebar.title("View Settings")

pdb_code = st.sidebar.text_input(
        label="PDB Code",
        value="1HQR",
    )
style = st.selectbox('style',['cartoon','line','cross','stick','sphere'])

resi_list = st.sidebar.multiselect(label="Highlight Residues",options=list(range(1,5000)))

chain = st.sidebar.text_input(label="Highlight Chain",value="A")

label_resi = st.sidebar.checkbox(label="Label Residues", value=True)

surf_transp = st.sidebar.slider("Surface Transparency", min_value=0.0, max_value=1.0, value=0.0)

hl_color = st.sidebar.text_input(label="Highlight Color",value="turquoise")

bb_color = st.sidebar.text_input(label="Backbone Color",value="yellow")
lig_color = st.sidebar.text_input(label="Ligand Color",value="magenta")

st.markdown(f"## PDB [{pdb_code.upper()}](https://www.rcsb.org/structure/{pdb_code}) (Chain {chain})")
        
prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
prot_list=prot_str.split(',')
protein=st.selectbox('Select a protein',prot_list)
style = st.selectbox('Select molecule style',['cartoon','line','cross','stick','sphere'])


### Step 3) Py3Dmol

width = 1000
height = 800

cartoon_radius = 0.2
stick_radius = 0.2

view = py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)
view.setStyle({"cartoon": {"style": "oval","color": "spectrum","thickness": cartoon_radius}})
view.setStyle({style:{'color':'spectrum'}})
view.addSurface(py3Dmol.VDW, {"opacity": surf_transp, "color": bb_color},{"hetflag": False})

view.addStyle({"elem": "C", "hetflag": True},
                {"stick": {"color": lig_color, "radius": stick_radius}})

view.addStyle({"hetflag": True},
                    {"stick": {"radius": stick_radius}})
for resi in resi_list:
    view.addStyle({"chain": chain, "resi": resi, "elem": "C"},
                    {"stick": {"color": hl_color, "radius": stick_radius}})

    view.addStyle({"chain": chain, "resi": resi},
                        {"stick": {"radius": stick_radius}})

if label_resi:
    for resi in resi_list:
        view.addResLabels({"chain": chain,"resi": resi},
        {"backgroundColor": "lightgray","fontColor": "black","backgroundOpacity": 0.5})

showmol(view, height=height, width=width)


st.markdown(f"## MOL PDB + Protein PDB [{protein.upper()}](https://www.rcsb.org/structure/{protein}) (Chain {chain})")


view1=py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)

view1=py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)
view1.addModelsAsFrames(open(f"PBDs/{protein.lower()}.pdb", 'r').read(),'pdb')
view.zoomTo()
view1.setBackgroundColor('white')
view1.setStyle({"cartoon": {"style": "oval","color": "spectrum","thickness": cartoon_radius}})
view1.setStyle({style:{'color':'spectrum'}})
#view1.setCameraParameters({ fov: 10 , z: 300 });
showmol(view1, height=height, width=width)
