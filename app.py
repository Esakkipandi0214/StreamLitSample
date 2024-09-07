import streamlit as st
from utils.auth import check_login_status, login_user, logout_user
from pages.dashboard import show_dashboard
from pages.login import show_login_page

# Initialize session state for user authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Application main function
def main():
    st.title("Streamlit Login & Dashboard App")
    
    if st.session_state.authenticated:
        # If user is logged in, show the dashboard
        show_dashboard()
        if st.button("Logout"):
            logout_user()
    else:
        # Show login page if user is not logged in
        show_login_page()

if __name__ == '__main__':
    main()
