import streamlit as st
import numpy as np
from uber_pickups import DATE_COLUMN
if "data" not in st.session_state:
    st.warning("No data avaiable, Please load data")
    st.stop()
data=st.session_state.data
st.header("📈 Graph")
st.subheader('Number of pickups by hour')
st.sidebar.header("Number of pickups by hour")
if DATE_COLUMN in data.columns:
    hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
else:
    st.bar_chart(data)