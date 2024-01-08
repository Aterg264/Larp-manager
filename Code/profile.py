import streamlit as st
import account

def createPage():
    st.header("Perfil")
    st.text('Nombre: ' + st.session_state.username)
    st.text('Correo: ' + st.session_state.useremail)
    st.button('Sign out', on_click=account.signout())
    