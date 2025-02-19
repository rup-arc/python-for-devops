import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# Check if there are enough arguments
if len(sys.argv) < 4:
    print("Usage: python script.py <num1> <operation> <num2>")
    sys.exit(1)

# Get the values from the command line arguments
try:
    num1 = float(sys.argv[1])
    operation = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: Please provide valid numbers for num1 and num2.")
    sys.exit(1)

# Perform the operation based on the user input
if operation == "add":
    output = add(num1, num2)
    print("Result:", output)
elif operation == "sub":
    output = sub(num1, num2)
    print("Result:", output)
elif operation == "mul":
    output = mul(num1, num2)
    print("Result:", output)
else:
    print(f"Unknown operation: {operation}. Please use 'add', 'sub', or 'mul'.")
