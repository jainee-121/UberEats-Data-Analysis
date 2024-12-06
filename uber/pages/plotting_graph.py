import streamlit as st
from uber_pickups import data,DATE_COLUMN,np
st.header("📈 Graph")
st.subheader('Number of pickups by hour')
st.sidebar.header("Number of pickups by hour")
hist_values = np.histogram(
data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)