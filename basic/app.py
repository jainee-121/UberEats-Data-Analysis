'''streamlits topic covered:
1. write/dataframe/table/header/subheaders/markdown/divider
2. linechart/map/scatter_plot
3. slider/button
4. selectbox/checkbox/radio
5. sidebar
6. columns
7. cache/session/color_picker
8. connection with db
9. pages

'''
import streamlit as st
import pandas as pd
import numpy as np

st.write("WLC, to streamlit")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

# Graph

st.table(dataframe)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


# Widgets

# st.slider(), st.button() or st.selectbox().
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# Use a selectbox for options
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option


# Layout

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column= st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


# Show progress
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

"...and now we're done "


# Caching

# st.cache_data - anything that can be stored in DB (list,str,dict,...)
# st.cache_resource -  anything that can not be stored in DB (models,...)

@st.cache_data
def long_running_function(param1, param2):
    return True


# Session State

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
 
st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


# connection

import streamlit as st

'''conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)'''

# Pages


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
