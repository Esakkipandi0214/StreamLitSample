import streamlit as st
from utils.auth import login_user

def show_login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login_user(username, password):
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password. Please try again.")
