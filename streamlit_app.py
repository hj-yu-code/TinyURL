import streamlit as st
import pyshorteners

# Streamlit 웹앱 제목 설정
st.title("URL Shortener")

# 사용자로부터 URL 입력받기
long_url = st.text_input("Enter the URL you want to shorten:")

# URL을 단축하는 버튼
if st.button("Shorten URL"):
    # pyshorteners를 이용해 URL 단축
    if long_url:
        s = pyshorteners.Shortener()
        try:
            short_url = s.tinyurl.short(long_url)
            st.success(f"Shortened URL: {short_url}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL")

# 하단에 긴 URL과 단축된 URL을 표시
if long_url:
    st.write("Original URL:", long_url)
