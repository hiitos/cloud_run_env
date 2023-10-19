import time 
import streamlit as st
from frontend.components import menu,auth,db

# ___________Loginの呼び出し____________
class Login:
    def __init__(self, db_path):
        self.controller = LoginController(db_path)
        self.controller.page_choice()

# ___________Loginのコントローラー___________
class LoginController:
    def __init__(self, db_path):
        self.model = db.UserDataBase(db_path)
        self.av = menu.LoginSideMenu()
        self.gu = auth.GeneralLoginView()
        self.au = auth.AdminLoginView()

    # 各ページのコントロール
    def _general(self):
        """
        アカウント認証が成功している場合st_sessionが更新される
        """
        self.gu.main_form()
        self.gu.side_form(self.model)
        auth = 'authentication_status'

        # アカウント認証に成功
        if st.session_state[auth]:
            st.balloons()
            st.success(f"ようこそ {st.session_state['name']} さん")
            with st.spinner('アカウント情報を検証中...'):
                time.sleep(0.5)
            st.experimental_rerun()

        # アカウント認証の情報が間違っているとき
        elif st.session_state[auth] == False:
            st.error("ログイン情報に誤りがあります。再度入力確認してください。")
            st.warning("アカウントをお持ちでない方は管理者に連絡しアカウントを作成してください")

        # アカウント認証の情報が何も入力されていないとき
        elif st.session_state[auth] is None:
            st.warning("アカウント情報を入力してログインしてください。")

    def _admin(self):
        admin_chk = self.au.side_form()
        # パスべた書き
        if admin_chk == "admin":
            self.au.main_form(self.model)
            if self.au.submit:
                res = self.model.add_user(self.au.name, self.au.username, self.au.password, self.au.adminauth)
                if res:
                    self.au.emp.success(res)
                else:
                    self.au.emp.warning("入力値に問題があるため、登録出来ませんでした")
        elif admin_chk == "":
            st.subheader("アクセスキーを入力してください")
        else:
            st.error("管理者キーが違います")

    # ページを切り替えた際に実行する関数を変える
    def page_choice(self):
        """
        ページの遷移
        """
        if self.av.choice_menu == self.av.main_menu[0]:
            self._general()
        if self.av.choice_menu == self.av.main_menu[1]:
            self._admin()
