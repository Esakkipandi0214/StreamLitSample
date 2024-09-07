import streamlit as st

# Simple authentication check (replace with actual authentication logic)
def login_user(username, password):
    if username == "admin" and password == "password":
        st.session_state.authenticated = True
        return True
    return False

def check_login_status():
    return st.session_state.authenticated

def logout_user():
    st.session_state.authenticated = False
    st.success("Logged out successfully.")
