import streamlit as st
st.set_page_config(
    page_icon = "image.png"
)
hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)
st.title("💁‍♂️Support:")
url = "https://linktr.ee/aliraza.ramzan"
link_text = st.write("My social handles⬇️")
st.write(f"({url})")