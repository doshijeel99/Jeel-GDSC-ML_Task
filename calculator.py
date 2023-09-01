import math
def calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error: Invalid input"
expression = input("Enter an arithmetic expression: ")
result = calculator(expression)
print("Result:", result)