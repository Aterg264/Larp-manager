# run the code from github link: streamlit run link

import streamlit as st
import pandas as pd

from backend import *

"""
Use dataframe to create a table in two different ways:
"""

st.write("Without st.write")
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

