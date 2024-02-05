import streamlit as st

def main():
    st.title("Trang web đơn giản")
    st.header("Chào mừng bạn đến với trang web của tôi!")
    
    # Hiển thị một nút nhấn
    if st.button("Click để thực hiện một hành động"):
        st.write("Hành động đã được thực hiện!")
    
    # Hiển thị một khung văn bản để nhập dữ liệu
    user_input = st.text_input("Nhập vào một giá trị")
    st.write("Giá trị đã nhập:", user_input)
    
    # Hiển thị một danh sách lựa chọn
    options = ["Lựa chọn 1", "Lựa chọn 2", "Lựa chọn 3"]
    selected_option = st.selectbox("Chọn một lựa chọn", options)
    st.write("Lựa chọn đã chọn:", selected_option)

if __name__ == '__main__':
    main()

