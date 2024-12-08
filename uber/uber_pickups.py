import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


b=st.selectbox("Select",("None","DATA URL","Upload file"))
file=st.sidebar.file_uploader("choose a file to upload",type="csv")
data=st.empty()
@st.cache_resource
def load_data():
    if b=="DATA URL":
        data = pd.read_csv(DATA_URL, nrows=1000)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase,axis=1, inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    if b=="Upload file":
        data=pd.read_csv(file)
        return data
    return st.write("select something nah!!")


st.sidebar.header("View Raw Data")

data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("View Raw Data")   
c=st.selectbox("Select Lat",("ALL",40.74,40.75,40.695))
if c=="ALL":
    st.write(data) 
else:
    data=data[data['lat']==c]
    st.write(data) 
