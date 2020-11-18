# To Do
# get user input
# calculate
# output values
from lwdcalculator import Calculator

calculate = Calculator()
user_input = calculate.get_input()


print("""
1. Add
2. Subtract
3. Multiply
4. Divide
""")

operation = input("Please choose an operation : ")

while isinstance(operation, str):
    try:
        operation = int(operation)
    except ValueError:
        operation = input("Input should contain numbers only, please try again : ")

# can be simplified with dictionary
if operation == 1:
    result = user_input[0] + user_input[1]
    print(result)
else:
    print("No valid operation chosen.")