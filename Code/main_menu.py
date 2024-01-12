import streamlit as st
import account
import frontend
import profile

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
selected = "Perfil"

if st.session_state['page']=="initial":
    account.login(auth)

else:
    
    if st.button('Sign out'):
        account.signout()
        if st.session_state['page']=="initial":
            account.login(auth)

    else:
        selected = st.selectbox(
        "Selecciona",
        menu_list
        )
        if selected == "Perfil":
            # st.session_state.login = True
            st.session_state.page = "profile"

            profile.createPage()

        elif selected == "Tareas":
            # st.session_state.login = True
            
            frontend.createPage()

    