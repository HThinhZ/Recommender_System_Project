import streamlit as st

# Kiểm tra xem session state 'page' đã tồn tại chưa, nếu chưa thì thiết lập nó.
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page):
    st.session_state.page = page

# Giao diện cho trang chủ
if st.session_state.page == 'home':
    st.title('Trang chủ')
    if st.button('Gửi'):
        navigate_to('second_page')

# Giao diện cho trang thứ hai
elif st.session_state.page == 'second_page':
    st.title('Trang thứ hai')
    if st.button('Trở về'):
        navigate_to('home')
