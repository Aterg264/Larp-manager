import streamlit as st
import pandas as pd
from google.cloud import firestore

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

st.button('Hit me') 

st.header('Hello 🌎!')
if st.button('Balloons?'):
    st.balloons()

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("../keys/firestore-key-app-tasks.json")

# Create a reference to the Google post.
doc_ref = db.collection("character_types").document("Broker")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())