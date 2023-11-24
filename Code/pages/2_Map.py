import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Map page 🎉")

st.markdown("### Coordinates")

# MAP
map_data = pd.DataFrame(
    np.array([[41, 2], [41, -0.9], [37, -4]]),
    columns=['lat', 'lon'])
st.write(map_data)
st.map(map_data)
