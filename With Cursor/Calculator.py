"""Simple calculator with a repeat loop."""

valid_ops = {"addition", "subtraction", "multiplication", "division"}

while True:
    operation = input("Enter operation (addition, subtraction, multiplication, division) or 'exit' to quit: ").strip().lower()
    if operation == "exit":
        print("Exiting the program.")
        break
    if operation not in valid_ops:
        print("Invalid operation. Please try again.")
        continue
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if operation == "addition":
            result = a + b
        elif operation == "subtraction":
            result = a - b
        elif operation == "multiplication":
            result = a * b
        else:  # division
            if b == 0:
                print("Error: Division by zero.")
                continue
            result = a / b
        print(f"Result: {result}")
    except ValueError:
        print("Invalid number. Please try again.")