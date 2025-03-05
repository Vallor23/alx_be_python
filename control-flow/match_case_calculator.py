num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

if operation == '+':
    print(f"The result is {num1 + num2}")
elif operation == '*':
    print(f"The result is {num1 * num2}")
elif operation == '-':
    print(f"The result is {num1 - num2}")
elif operation == '/':
    try:
        print(f"The result is {num1 / num2}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")