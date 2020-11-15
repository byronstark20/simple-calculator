# To Do
# get user input
# calculate
# output values


values = input("Please enter two numbers : ")
values = [int(i) for i in values.split()]
print(values)
print("""
1. Add
2. Subtract
3. Multiply
4. Divide
""")
operation = input("Please choose an operation : ")

while operation.isalpha() :
    operation = input("Invalid input, please try again : ")
operation = int(operation)

# can be simplified with dictionary
if operation == 1:
    result = values[0] + values[1]
    print(result)
else:
    print("No valid operation chosen.")