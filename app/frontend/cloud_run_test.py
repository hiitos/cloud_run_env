# streamlitのサンプルUIのコードを記述
import streamlit as st

def test():
    # タイトルを設定する
    header = st.container()
    with header:
        title,menu = st.columns([3,1])
        title.title("Cloud Run Test")
        selected_option = menu.selectbox('', ['menu1', 'menu2', 'menu3'])
        st.markdown('---')
        st.markdown('')
        st.markdown('')
        st.markdown('')

    # サイドメニューを設定する
    sidebar = st.sidebar
    sidebar.markdown('---')
    # ボタンの作成
    button = sidebar.button('btn')