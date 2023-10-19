from PIL import Image
import streamlit as st
import streamlit_authenticator as stauth

# ___________Loginのメインの表示____________
class GeneralLoginView:
    def main_form(self):
        st.header("ようこそ！")
        # logo = Image.open(path)
        # st.image(logo, use_column_width=True)

    def side_form(self, model):
        """
        認証フォームの表示
        """
        credentials = {"usernames":{}}
        for uname,name,pwd in zip(model.df[model.username], model.df[model.name], model.df[model.password]):
            credentials["usernames"][uname] = {"name":name, "password":pwd}

        self.authenticator = stauth.Authenticate(
            credentials,
            'some_cookie_name', 
            'some_signature_key', 
            cookie_expiry_days=0)
        self.authenticator.login("ログイン", "sidebar")

# ___________Adminのメインの表示____________
class AdminLoginView:
    def main_form(self, model):
        with st.form(key="create_acount"):
            st.subheader("新規ユーザの作成")
            self.name = st.text_input("ニックネームを入力してください", key="create_name")
            self.username = st.text_input("ユーザー名(ID)を入力してください", key="create_username")
            self.password = st.text_input("パスワードを入力してください",type='password', key="create_pass")
            self.adminauth = st.checkbox("管理者権限の付与")
            self.submit = st.form_submit_button(label='アカウントの作成')
        self.emp = st.empty()

        with st.expander("ユーザテーブルを表示"):
            model.get_table()
            st.table(model.df.drop(model.password, axis=1))

    def side_form(self):
        st.sidebar.write("---")
        st.sidebar.info("adminがキーです")
        return  st.sidebar.text_input("管理者アクセスキー" ,type='password')