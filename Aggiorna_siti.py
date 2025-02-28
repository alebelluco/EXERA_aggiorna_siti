import streamlit as st
import pandas as pd 
from utils import persistence_ab as pe 
st.set_page_config(layout='wide')
st.title('Aggiornamento siti')



cred = st.sidebar.file_uploader('credenziali')
if not cred:
    st.stop()
credenziali=pd.read_excel(cred)

file_path  = credenziali.Dati.iloc[3]
username = credenziali.Dati.iloc[0]
repository_name  = credenziali.Dati.iloc[2]
token = credenziali.Dati.iloc[1]

path =  st.file_uploader('Caricare file siti estratto da Byron')
if not path:
    st.stop()
file = pd.read_excel(path)
#st.write(siti_aggiornato

if st.button('Aggiorna'):
    pe.upload_file(username, token, file, repository_name, file_path)


path2='https://github.com/alebelluco/Test_EX/blob/main/cantieri_aggiornato?raw=True'

#siti = pd.read_pickle(path2)

if st.toggle('Visualizza siti con problemi'):
    st.subheader('Coordinate a zero')
    file = file[file.servizi != 0]

    mask = file.columns[:10]
    st.dataframe(file[mask][file.lat==0], use_container_width=True)

    st.subheader('Coordinate mancanti')
    st.dataframe(file[mask][file.lat.astype(str)=='nan'], use_container_width=True)

