def perform_operation(num1,num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return ValueError("Cannot divide by zero")
        else:
            return num1 / num2
    else:
        return "Invalid operation"
    