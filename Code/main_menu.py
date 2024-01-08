import streamlit as st
import account
import frontend
from streamlit_option_menu import option_menu

# menu_list = ["Perfil", "QR", "Tareas", "Histórico de tareas", "Zonas"]
menu_list = ["Perfil", "Tareas"]

with st.sidebar:

    selected = option_menu(
        menu_title=None,
        options=menu_list
        )

# if st.session_state['signout']:
if selected == "Perfil":
    account.createPage()

if selected == "Tareas":
    frontend.createPage()