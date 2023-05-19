import streamlit as st
st.set_page_config(
    page_icon = "ℹ️"
)
hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)
st.title("ℹ️ About")
st.write("Discover a healthier lifestyle with our Nutrition Diet Timetable Generator. Easily create personalized diet plans tailored to your specific nutritional needs. Take control of your meals, track your calorie intake, and achieve your wellness goals with ease. Start your journey towards a balanced and nourishing diet today!")
st.write("Created by: Ali Raza")