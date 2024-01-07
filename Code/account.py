import pyrebase
import streamlit as st

firebaseConfig={
  'apiKey': "AIzaSyBN7u_CoR0NAEpVlkrvGqPOhj1oQK1xJlk",
  'authDomain': "tasks-594c6.firebaseapp.com",
  'databaseURL': "http://tasks-594c6.firebaseapp.com",
  'projectId': "tasks-594c6",
  'storageBucket': "tasks-594c6.appspot.com",
  'messagingSenderId': "356007745177",
  'appId': "1:356007745177:web:b59e18bffa3647ee2c8a08",
  'measurementId': "G-QE8N8LH6KT"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login():
    st.title("Lunbapp")

    def check():
        try:
            login = auth.sign_in_with_email_and_password(email,password)
            st.write("Login realizado")
        except:
            st.warning("Datos incorrectos")

    email = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    st.button("Login", on_click=check)

login()