def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    expression = input("Enter an expression (e.g. 4 + 5): ")
    parts = expression.split()
    if len(parts) != 3:
        print("Invalid input format. Use: number operator number")
        return

    try:
        x = float(parts[0])
        op = parts[1]
        y = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter numeric values.")
        return

    try:
        if op == "+":
            result = add(x, y)
        elif op == "-":
            result = subtract(x, y)
        elif op == "*":
            result = multiply(x, y)
        elif op == "/":
            result = divide(x, y)
        else:
            print("Unsupported operator. Use +, -, *, or /")
            return

        print(f"Result: {result}")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
