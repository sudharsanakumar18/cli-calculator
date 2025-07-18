import sys

def calculate(op, x, y):
    x, y = float(x), float(y)
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    elif op == 'mul':
        return x * y
    elif op == 'div':
        return x / y if y != 0 else "Error: Division by zero"
    else:
        return "Error: Unknown Operation"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python cli_calculator.py <operation> <num1> <num2>")
        print("Operations: add, sub, mul, div")
    else:
        _, op, num1, num2 = sys.argv
        result = calculate(op, num1, num2)
        print("Result:", result)
