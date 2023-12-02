import streamlit as st
import pandas as pd
import numpy as np
import time
# from google.cloud import firestore

from backend import *

st.sidebar.markdown("# Main page 🎈")
st.header('Hello 🌎!!')

"""
Use dataframe to create a table in two different ways
"""

st.write("Without st.write:")
df = pd.DataFrame({
  'first column': [number(), 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

st.write("Using st.write")
st.write(pd.DataFrame({
    'first column': [number(), 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# SEARCHER SIDEBAR

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
"""

# TWO COLUMNS LAYOUT

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



