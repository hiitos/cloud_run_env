import streamlit as st
from PIL import Image
from frontend.pages import login
from frontend.cloud_run_test import test


# 環境変数を設定する
# image = Image.open(path)
st.set_page_config(
    page_title="Cloud Run Test",
    # page_icon=image,
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():

    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None

    print(st.session_state['authentication_status'])
    # ログイン認証に成功すれば処理切り替え
    if st.session_state['authentication_status']:
        # こにメインのアプリ機能を書く
        test()
        # 別途ログアウトボタンを実装
        if st.sidebar.button("ログアウト"):
            st.session_state['authentication_status'] = None
            st.experimental_rerun()
    else:
        login.Login("login_db/user.db")

if __name__ == '__main__':
    main()