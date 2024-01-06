import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("./firestore-key-app-tasks.json")
#firebase_admin.initialize_app(cred)
    

def account():

    def f():
        try:
            user = auth.get_user_by_email(email)
            st.write("Login realizado")

        except:
            st.warning("Datos de usuario incorrectos")

    st.title("Lunbapp")

    email = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    st.button("Login", on_click=f)

account()
