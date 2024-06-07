import streamlit as st
import base64

# Hàm để đọc file hình ảnh và chuyển đổi sang base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
# Hàm để tạo và hiển thị các cột
def display_columns(items, cols=3):
    for i in range(0, len(items), cols):
        cols_list = st.columns(cols)
        for j, col in enumerate(cols_list):
            if i + j < len(items):
                # Đường dẫn tới hình ảnh cục bộ
                local_image_path = "images\image1.jpg"

                # URL đích khi nhấp vào hình ảnh
                link_url = "https://www.facebook.com/"

                # Chuyển đổi hình ảnh sang base64
                local_image_base64 = get_image_base64(local_image_path)

                # Sử dụng HTML để chèn hình ảnh, thêm caption và liên kết
                image_html = f'''
                    <a href="{link_url}" target="_blank">
                        <img src="data:image/jpeg;base64,{local_image_base64}" width="100%">
                        <div style="text-align:center;">{items['title'][i+j]}</div>
                    </a>
                '''
                with col:
                    st.markdown(image_html, unsafe_allow_html=True)