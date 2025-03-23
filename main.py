# prompt:  Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

! pip install streamlit

import streamlit as st

def calculate_bmi(weight, height):
  """Calculates the Body Mass Index (BMI)."""
  try:
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)
  except ZeroDivisionError:
    return "Invalid input. Height cannot be zero."

def main():
  st.title("BMI Calculator")

  st.write("Enter your weight and height to calculate your BMI.")

  weight = st.number_input("Weight (kg):", min_value=0.0, step=0.1)
  height = st.number_input("Height (cm):", min_value=0.0, step=0.1)

  if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi}")

    if bmi < 18.5:
      st.write("You are underweight.")
    elif bmi < 25:
      st.write("You are in a healthy weight range.")
    elif bmi < 30:
      st.write("You are overweight.")
    else:
      st.write("You are obese.")

if __name__ == "__main__":
  main()
