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

if not st.session_state['login']:
    account.login(auth)
    st.sidebar.markdown("# Login")

# menu_list = ["Perfil", "QR", "Tareas", "Histórico de tareas", "Zonas"]
menu_list = ["Perfil", "Tareas"]

if st.session_state['page']!="initial":
    with st.sidebar:

        selected = option_menu(
            menu_title=None,
            options=menu_list
            )

    if selected == "Perfil":
        # st.session_state.login = True
        st.session_state.page = "profile"

        profile.createPage()

    if selected == "Tareas":
        # st.session_state.login = True
        st.session_state.page = "tasks"

        frontend.createPage()