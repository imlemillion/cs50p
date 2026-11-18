expression = input("Expression: ").split()

if len(expression) != 3:
    print("Please use the format: number operator number")
else:
    x = float(expression[0])
    operator = expression[1]
    z = float(expression[2])

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        if z == 0:
            result = "Error: cannot divide by zero."
        else:
            result = x / z
    else:
        result = "Error: operator not recognized."
    print(result)
