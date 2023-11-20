import streamlit as st
import pandas as pd
import numpy as np
import time
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

# st.button('Hit me') 

st.header('Hello 🌎!')
if st.button('Balloons?'):
    st.balloons()

if st.button('Snow?'):
    st.snow()

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

# Create a map
map_data = pd.DataFrame(
    np.array([[41, 2], [41, -0.9], [37, -4]]),
    columns=['lat', 'lon'])
st.write(map_data)
st.map(map_data)

# PLAYING WITH FIREBASE

# Observe Data

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("./keys/firestore-key-app-tasks.json")

# Create a reference to the Google post.
doc_ref = db.collection("character_type").document("Broker")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

""""
# Create New Data

# Create a new post reference for Organizacion
doc_ref = db.collection("character_type").document("Organizacion")

# And then uploading some data to that reference
doc_ref.set({
  "code": "organizacion",
  "funcion": "organizar"
})

"""

# 

# Streamlit widgets to let a user create a new post
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

# Once the user has submitted, upload it to the database
if title and url and submit:
	doc_ref = db.collection("posts").document(title)
	doc_ref.set({
		"title": title,
		"url": url
	})

# And then render each post, using some light Markdown
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]({url})")