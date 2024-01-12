import streamlit as st
import account
import frontend
import profile
from streamlit_option_menu import option_menu

auth = account.firebase_configuration()

if 'login' not in st.session_state:
    st.session_state.login = False
if 'page' not in st.session_state:
    st.session_state.page = "initial"

if 'username' not in st.session_state:
    st.session_state.username = ''
if 'useremail' not in st.session_state:
    st.session_state.useremail = ''

# menu_list = ["Perfil", "QR", "Tareas", "Histórico de tareas", "Zonas"]
menu_list = ("Perfil", "Tareas")

if st.session_state['page']=="initial":
    account.login(auth)
else:

    selected = st.selectbox(
        "Selecciona",
        menu_list
        )
    
    if st.button('Sign out'):
        account.signout()

    elif selected == "Perfil":
        # st.session_state.login = True
        st.session_state.page = "profile"
        st.write(st.session_state.login)
        st.write(st.session_state.page)

        profile.createPage()

    elif selected == "Tareas":
        # st.session_state.login = True
        st.session_state.page = "tasks"

        frontend.createPage()

    