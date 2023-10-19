import streamlit as st

# ___________Loginのサイドバーの表示____________
class LoginSideMenu:
    def __init__(self):
        self.main_menu = ["Login", "Admin", "Contact"]
        self.choice_menu = st.sidebar.selectbox("メニュー", self.main_menu)