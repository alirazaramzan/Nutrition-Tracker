import streamlit as st
st.set_page_config(
    page_icon = "📱"
)
hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)
st.title("📱Contact:")
st.write("📧 Email: aliunknown55@gmail.com")

st.write("*If you want to give any suggestions or need any help feel free to reach me out through my e-mail!*")
