#1
print('Exercise 1')
name = input(" What is your name ")
surname = input(" What is your surname ")
age = input(" What is your age ")
print(f"Your name is {name} {surname},and you are {age} years old")


#2
print('Exercise 2')
fahreanheit = float(input("Enter temperature in fahreanheit: "))
celsius = (fahreanheit  -32)*5 /9
print("Temperature in  Celsius:", celsius)


#3
print('Exercise 3')
# Gather individual scores
work_in_class_score = float(input("Enter your work in class score: "))
test_score = float(input("Enter your test score: "))
project_score = float(input("Enter your project score: "))

# Calculate the final score based on the weightings
final_score = (work_in_class_score * 0.20) + (test_score * 0.30) + (project_score * 0.50)

# Determine the grade based on the Polish grading system
if final_score >= 90:
    grade = 5  #  - very good
elif final_score >= 75:
    grade = 4  #  - good
elif final_score >= 60:
    grade = 3  #  - satisfactory
elif final_score >= 50:
    grade = 2  #  - failing
else:
    grade = 1  #  - failing

# Print the grade
print("Your grade is:", grade)
#4
print('Exercise 4')
# Define variables
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Check if the first number is divisible by the second
if number2 != 0:  # Ensure the second number is not zero to avoid division by zero error
    if number1 % number2 == 0:
        result = "Divisible"
    else:
        result = "Not divisible"
else:
    result = "Error: Division by zero is not allowed."

# Print the result
print("The result is:", result)

# Print the result
print("The number is:", result)
#5
print('Exercise 5')
# Prompt the user to enter values of different types
var_int = int(input("Enter an integer value: "))
var_float = float(input("Enter a float value: "))
var_str = input("Enter a string value: ")
var_bool = input("Enter a boolean value (True or False): ").lower() == "true"

# Determine the type of each variable
type_int = type(var_int).__name__
type_float = type(var_float).__name__
type_str = type(var_str).__name__
type_bool = type(var_bool).__name__

# Print the type of each variable
print("Type of var_int:", type_int)
print("Type of var_float:", type_float)
print("Type of var_str:", type_str)
print("Type of var_bool:", type_bool)
#6
print('Exercise 6')
# Define variables
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if a triangle can be drawn
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # If a triangle can be drawn, check the type of triangle
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    print("The triangle is:", triangle_type)
else:
    print("A triangle cannot be formed with the given sides.")

# Print the type of triangle
print("The triangle is:", triangle_type)

#7
print("Exercise 7")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("Result:", result)