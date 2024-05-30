import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
 # Title of the app
st.title("Student Information")
# Text input for student's name
student_name = st.text_input("Enter the student's name:")

# Slider for student's age
student_age = st.slider("Select the student's age:", 1, 100)

# Button to display the input text and age
if st.button("Display Information"):
    st.write("Student's name: ",student_name)
    st.write("Student's age: ",student_age)
