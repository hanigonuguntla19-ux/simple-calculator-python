"""
Simple Calculator
A command-line calculator built using Python.

Author: Hani Gonuguntla
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result."""
    if b == 0:
        return None
    return a / b


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("          PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)


def calculator():
    """Run the calculator application."""

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using Python Calculator!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select a number from 1 to 5.")
            continue

        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(first_number, second_number)
            operator = "+"

        elif choice == "2":
            result = subtract(first_number, second_number)
            operator = "-"

        elif choice == "3":
            result = multiply(first_number, second_number)
            operator = "*"

        else:
            result = divide(first_number, second_number)
            operator = "/"

            if result is None:
                print("Error: Division by zero is not allowed.")
                continue

        print(
            f"\nResult: {first_number:g} "
            f"{operator} {second_number:g} = {result:g}"
        )

if __name__ == "__main__":
    calculator()
