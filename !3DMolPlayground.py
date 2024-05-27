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





obj = render_pdb(id = '1A2C')
obj = render_pdb_resn(obj ,resn_lst = ['ALA',])
showmol(obj,height = 800,width=800)
                                                                    

                                                                    
                                                                    
