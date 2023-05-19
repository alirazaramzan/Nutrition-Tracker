import streamlit as st
import time
st.set_page_config(page_title='Nutrition Diet Timetable Generator', page_icon='🍴')
hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height /= 100

    # Calculate BMI
    bmi = weight / (height * height)
    return bmi

def generate_diet_timetable(weight, height):
    bmi = calculate_bmi(weight, height)

    # Generate diet timetable based on BMI
    if bmi < 18.5:
        with st.spinner("Loading..."):
                time.sleep(5)
        url = "https://dawaai.pk/doctors-online"
        st.warning("Please consult with a doctor, through this link")
        link_text = st.write("Visit site")
        st.write(f"({url})")
        timetable = "You are underweight. Here's a sample diet plan:\n- Breakfast: Oatmeal with fruits\n- Snack: Greek yogurt with nuts, Protein Shake, Mixed berries\n- Lunch: Grilled chicken with vegetables\n- Dinner: Baked fish with quinoa"

    elif 18.5 <= bmi < 24.9:
        timetable = "You have a normal weight. Here's a sample diet plan:\n- Breakfast: Whole grain toast with avocado\n- Snack: Apple with peanut butter, Hummus with carrots, Dark chocolate\n- Lunch: Salad with grilled tofu\n- Dinner: Quinoa with roasted vegetables"
    elif 24.9 <= bmi < 29.9:
        timetable = "You are overweight. Here's a sample diet plan:\n- Breakfast: Scrambled eggs with vegetables\n- Snack: Almonds, Greek yogurt with honey, Edamame beans\n- Lunch: Brown rice with lean meat\n- Dinner: Grilled salmon with steamed broccoli"
    else:
        with st.spinner("Loading..."):
                time.sleep(5)
        url = "https://dawaai.pk/doctors-online"
        st.warning("Please consult with a doctor, through below link")
        link_text = st.write("Visit site")
        st.write(f"({url})")
        timetable = "You are obese. Here's a sample diet plan:\n- Breakfast: Green smoothie with spinach and banana\n- Snack: Rice cakes with almond butter, Mixed nuts, Sliced watermelon\n- Lunch: Quinoa salad with chickpeas\n- Dinner: Grilled chicken with sweet potato"

    return timetable

# Streamlit app code
def main():
    st.title("🍴Nutrition Diet Timetable Generator")
    st.write("Enter your weight and height to generate a nutritional diet timetable.")

    weight = st.number_input("Weight (in kg)")
    height = st.number_input("Height (in cm)")

    if weight <= 0 or height <= 0:
        st.warning("Please enter valid weight and height.")
    else:
        if st.button("Generate Timetable"):

            timetable = generate_diet_timetable(weight, height)
            with st.spinner("Loading..."):
                time.sleep(5)
            st.subheader("Your Diet Timetable:")
            st.write(timetable)

if __name__ == "__main__":
    main()
