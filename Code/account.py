import streamlit as st
import firebase_admin

from google.cloud import firestore
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate("./firestore-key-app-tasks.json")
# firebase_admin.initialize_app(cred)

def account():

    def check():
        try:
            login = auth.get_user_by_email(email)
            st.write(login.uid)
            st.write("Login realizado")
        except:
            st.warning("Datos incorrectos")

    st.title("Lunbapp")

    email = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    st.button("Login", on_click=check)


account()   
page = auth.list_users()
while page:
    for user in page.users:
        st.write('User: ' + user.uid)
    # Get next batch of users.
    page = page.get_next_page()

user = auth.get_user("874joVGUMtXVrvNKBfex3ZPQTWz1")
st.write("user email: ", user.email)
