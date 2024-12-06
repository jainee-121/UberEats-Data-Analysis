import streamlit as st
from uber_pickups import *
data = load_data(10000)
st.markdown("# :earth_asia: MAP")
st.sidebar.header("Look at our Map")

hour_to_filter = st.slider('Slide to change Hours', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

