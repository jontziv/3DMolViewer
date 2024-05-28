import streamlit as st
from st_speckmol import speck_plot 
from stmol import showmol,render_pdb,render_pdb_resn


obj = render_pdb(id = '1A2C')
obj = render_pdb_resn(obj ,resn_lst = ['ALA',])
showmol(obj,height = 800,width=800)
                                                                    

                    


