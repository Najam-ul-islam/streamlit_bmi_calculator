import streamlit as st
import time


# set the layout of the page
col1,col2 = st.columns([0.6,0.4], gap='medium')
# ========================== Title ==========================
title_container = st.container(border=True)
with col1:
    # set the title of the page
    title_container.header("BMI Calculator")
# ========================== User Input ========================== 
# get the weight and height from the user
one_ft: float = 0.3048
weight_kg: float = col1.number_input("Weight(Kg): ")
height_ft: float = col1.number_input("Height(ft): ")
# ========================== Convert Feet to Meters ==========================
# convert feet to meters
height_meter = height_ft * one_ft
# ========================== BMI Calculator Function ==========================
# define a function
def bmi_calculator(weight: float, height: float) -> float:
    
    """ Calculates the BMI based on the weight and height."""    
    # using the pattern matching feature of Python to overcome the  zero division error
    match height:
        case 0.0:
            return 0.0
        case _:
            pass
    bmi = weight / (height ** 2)
    return bmi
# ========================== BMI Function Call ==========================
bmi = bmi_calculator(weight_kg, height_meter)
btn = col1.button("Calculate BMI")
# check if the button is clicked
if btn:
    # show the progress bar
    with st.spinner("Calculating BMI..."):
    # wait for 1 seconds
        time.sleep(1)
    # show the result
    col1.success(f"BMI: {bmi:.2f}")
    # show the category
    match bmi:
        case (bmi) if (bmi < 18.5):
            col1.warning("You are Underweight")
        case (bmi) if (bmi >= 18.5 and bmi < 24.9):
            col1.success("You are Normal")
        case (bmi) if (bmi >= 25 and bmi < 29.9):
            col1.warning("You are Overweight")
        case _:
            col1.warning("You are Obese")
# ========================== BMI Categories ==========================
# display the info of BMI categories
col2.info("BMI Categories:")
col2.markdown("- Underweight < 18.5")
col2.markdown("- Normal weight 18.5 – 24.9")
col2.markdown("- Overweight 25 – 29.9")
col2.markdown("- Obesity 30 or greater")

# ========================== Unit Conversion ==========================
# display the info of unit conversion
# st.sidebar.radio("Unit Conversion", options=["centimeter(cm) to meters(m)", "meters(m) to centimeter(cm)","kilogram(kg) to pounds(lbs)","pounds(lbs) to kilogram(kg)","feet(ft) to meters(m)","meter(m) to feet(ft)"])
# ========================== Unit Conversion Function ==========================
class UnitConversion:
    """This class converts the units."""
    # define a function
    def __init__(self, unit: float) -> None:
        self.unit = unit
    # define a function
    def cm_to_m(self) -> float:
        """Converts centimeter to meters."""
        return self.unit / 100
    # define a function
    def m_to_cm(self) -> float:
        """Converts meters to centimeter."""
        return self.unit * 100
    # define a function
    def kg_to_lbs(self) -> float:
        """Converts kilogram to pounds."""
        return self.unit * 2.20462
    # define a function
    def lbs_to_kg(self) -> float:
        """Converts pounds to kilogram."""
        return self.unit / 2.20462
    # define a function
    def ft_to_m(self) -> float:
        """Converts feet to meters."""
        return self.unit * 0.3048
    # define a function
    def m_to_ft(self) -> float:
        """Converts meters to feet."""
        return self.unit / 0.3048
    
# ========================== Unit Conversion Function Call ==========================
# get the user input
unit = st.sidebar.number_input("Enter the unit number: ")
# call the function
unit_conversion = UnitConversion(unit)
# ========================== Unit Conversion Radio Buttons ==========================
# display the radio buttons
unit_options = st.sidebar.radio("Unit Conversion", options=["cm to m", "m to cm","kg to lbs","lbs to kg","ft to m","m to ft"])
# ========================== Unit Conversion Radio Buttons Function Call ==========================
# check if the radio button is clicked
if unit_options == "cm to m":
    # call the function
    result = unit_conversion.cm_to_m()
    # show the result
    st.sidebar.success(f"{unit} cm \t->\t {result:.2f} m")
elif unit_options == "m to cm":
    # call the function
    result = unit_conversion.m_to_cm()
    # show the result
    st.sidebar.success(f"{unit} m = {result:.2f} cm")
elif unit_options == "kg to lbs":
    # call the function
    result = unit_conversion.kg_to_lbs()
    # show the result
    st.sidebar.success(f"{unit} kg = {result:.2f} lbs")
elif unit_options == "lbs to kg":
    # call the function
    result = unit_conversion.lbs_to_kg()
    # show the result
    st.sidebar.success(f"{unit} lbs = {result:.2f} kg")
elif unit_options == "ft to m":
    # call the function
    result = unit_conversion.ft_to_m()
    # show the result
    st.sidebar.success(f"{unit} ft = {result:.2f} m")
elif unit_options == "m to ft":
    # call the function
    result = unit_conversion.m_to_ft()
    # show the result
    st.sidebar.success(f"{unit} m = {result:.2f} ft")
else:
    pass
# ========================== About ==========================
# display the info of the app
st.sidebar.info("This app is created by 'Muhammad Najam Ul Islam'")
