# To Do
# get user input
# calculate
# output values

values = input("Please enter two numbers : ")

while isinstance(values, str):
    try:
        values = [int(i) for i in values.split()]
    except ValueError:
        values = input("Input should contain numbers only, please try again : ")

print(values)
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
    result = values[0] + values[1]
    print(result)
else:
    print("No valid operation chosen.")