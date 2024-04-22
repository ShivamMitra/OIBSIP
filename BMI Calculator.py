def calculate_bmi(weight, height):
  """
  Calculates the Body Mass Index (BMI) given weight and height.

  Args:
    weight: Weight in kilograms (kg).
    height: Height in meters (m).

  Returns:
    The calculated BMI as a float.
  """
  return weight / height**2

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate the BMI
bmi = calculate_bmi(weight, height)

# Print the BMI and interpret it
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
  print("You are underweight.")
elif bmi < 25:
  print("You are in the healthy weight range.")
elif bmi < 30:
  print("You are overweight.")
else:
  print("You are obese.")

# Disclaimer
print("Note: This is a general BMI calculator and should not be used for medical diagnosis. Consult a healthcare professional for personalized advice.")