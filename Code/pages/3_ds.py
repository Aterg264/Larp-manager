import streamlit as st

st.markdown("# Ds page 🎉")
st.sidebar.markdown("# Ds page 🎉")

"""
# PLAYING WITH FIREBASE

# Observe Data

# Authenticate to Firestore with the JSON account key.
# st.write(os.chdir("C:/Users/Greta/Desktop/rol/Chains/Techie/Tasks_Chains"))
db = firestore.Client.from_service_account_json("keys/firestore-key-app-tasks.json")



# Create a reference to the Google post.
doc_ref = db.collection("character_type").document("Broker")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())


# Create New Data

# Create a new post reference for Organizacion
doc_ref = db.collection("character_type").document("Organizacion")

# And then uploading some data to that reference
doc_ref.set({
  "code": "organizacion",
  "funcion": "organizar"
})



# 

# Streamlit widgets to let a user create a new post
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

# And then render each character type, using some light Markdown
type_ref = db.collection("character_type")
for doc in type_ref.stream():
	type = doc.to_dict()
	code = type["code"]
	funcion = type["funcion"]

	st.subheader(f"Code: {code}")
	st.write(f":Funcion: [{funcion}]({funcion})")
"""