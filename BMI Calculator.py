def value_check(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def bmi_calculator():
    
    height = value_check("Enter your height (in meters): ", min_value=0.5, max_value=2.5)
    weight = value_check("Enter your weight (in kilograms): ", min_value=20, max_value=300)

    bmi = calculate_bmi(height, weight)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"This is classified as: {category}")

bmi_calculator()
