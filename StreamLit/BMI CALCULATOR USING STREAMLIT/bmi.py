# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator Using StreamLit')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input('Feet')

    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if bmi < 16:
        st.error("You are Severely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("You have Normal weight")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    elif 30 <= bmi < 35:
        st.error("You are Moderately Obese")
    elif 35 <= bmi < 40:
        st.error("You are Severely Obese")
    elif bmi >= 40:
        st.error("You are Morbidly Obese")

