import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

def account():

    st.title("Lunbapp")

    email = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    st.button("Login")
