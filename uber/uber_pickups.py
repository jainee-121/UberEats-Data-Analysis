import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

if "selected" not in st.session_state:
    st.session_state.selected="None"
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame() 

b=st.selectbox("Select",("None","DATA URL","Upload file"),index=["None", "DATA URL", "Upload file"].index(st.session_state.selected))

if b != st.session_state.selected:
    st.session_state.selected = b
    st.session_state.data = pd.DataFrame()
    
file= st.file_uploader("Choose a file to upload", type="csv") if b == "Upload file" else None

@st.cache_resource
def load_data(b,file):
    if b=="DATA URL":
        data = pd.read_csv(DATA_URL, nrows=1000)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase,axis=1, inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    elif b=="Upload file" and file is not None:
        data=pd.read_csv(file)
        return data
    return pd.DataFrame()

st.sidebar.header("View Raw Data")
data_load_state = st.text('Loading data...')    
if st.session_state.selected != "None" and st.session_state.data.empty:
    st.session_state.data = load_data(st.session_state.selected,file)
data = st.session_state.data
data_load_state.text("View Raw Data" if not data.empty else "No data available.")    

if not data.empty:
    if st.session_state.selected=="DATA URL":
        c=st.selectbox("Select Lat",("ALL",40.74,40.75,40.695))
        if c=="ALL":
            st.write(data) 
        else:
            data=data[data['lat']==c]
            st.write(data) 
    elif st.session_state.selected=="Upload file":
        c=st.selectbox("Select Age",("ALL",30,40,60))
        if c=="ALL":
            st.write(data) 
        else:
            data=data[data.Age==c]
            st.write(data) 
else:
    st.warning("No data available to display.")
