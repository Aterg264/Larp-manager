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
            user = auth.sign_in_with_email_and_password(email,password)
            st.write("Login realizado")

            st.session_state.username = user.get("localId")
            st.session_state.usermail = user.get("email")

            st.session_state.signedout = True
            st.session_state.signout = True
            # st.session_state.username = ''
            # st.session_state.useremail = ''

            # Information about account
            # st.write(auth.get_account_info(user['idToken']))
            # Information about localId and email account
            # st.write(user.get("localId"))
            # st.write(user.get("email"))
        except:
            st.warning("Datos incorrectos")

    email = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    st.button("Login", on_click=check)


def signout():
    st.session_state.signedout = False
    st.session_state.signout = False
    st.session_state.username = ''
    st.session_state.useremail = ''


if 'signedout' not in st.session_state:
    st.session_state.signedout = False
if 'signout' not in st.session_state:
    st.session_state.signout = False

if not st.session_state['signedout']:
    login()
if st.session_state['signout']:
    st.text('Nombre: ' + st.session_state.username)
    st.text('Correo: ' + st.session_state.useremail)
    st.button('Sign out', on_click=signout())

if 'username' not in st.session_state:
    st.session_state.username = ''
if 'useremail' not in st.session_state:
    st.session_state.useremail = ''

