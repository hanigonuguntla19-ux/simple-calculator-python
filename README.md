Simple Calculator Python

A clean and interactive command-line calculator built with Python that performs basic arithmetic operations with input validation and error handling.

Project Overview

The Simple Calculator Python project is a command-line application designed to perform fundamental mathematical operations.

The project demonstrates important Python programming concepts such as functions, loops, conditional statements, exception handling, user input validation, and modular programming.

The application provides a simple menu where users can select an operation, enter two numbers, and view the result.

Key Features

- Addition
- Subtraction
- Multiplication
- Division
- Continuous calculations
- Division-by-zero protection
- Invalid input handling
- Modular functions for each operation
- Command-line interface
- Exit option

Technologies Used

Technology| Purpose
Python 3| Application development
Git| Version control
GitHub| Source code hosting

Project Structure

simple-calculator-python/
│
├── calculator.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    └── calculator-output.png

How It Works

The calculator follows a simple workflow:

User
  |
  v
Display Menu
  |
  v
Select Operation
  |
  v
Enter Two Numbers
  |
  v
Validate Input
  |
  v
Perform Calculation
  |
  v
Display Result
  |
  v
Continue or Exit

Supported Operations

Option| Operation| Example
1| Addition| 10 + 5 = 15
2| Subtraction| 10 - 5 = 5
3| Multiplication| 10 * 5 = 50
4| Division| 10 / 5 = 2
5| Exit| Close application

Python Concepts Demonstrated

- Functions
- Parameters and return values
- While loops
- Conditional statements
- User input
- Exception handling
- Input validation
- String formatting
- Modular programming
- Error handling

Error Handling

The calculator handles common input errors safely.

Invalid Menu Selection

If the user enters an option other than 1–5, the application displays an error message and asks for another choice.

Invalid Number Input

If the user enters text instead of a number, the application handles the error without crashing.

Division by Zero

The application prevents division by zero and displays an appropriate error message.

Sample Output

========================================
          PYTHON CALCULATOR
========================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
========================================

Enter your choice (1-5): 1
Enter first number: 25
Enter second number: 15

Result: 25 + 15 = 40

Division by Zero

Enter your choice (1-5): 4
Enter first number: 20
Enter second number: 0

Error: Division by zero is not allowed.

Screenshots

Add your calculator screenshot to the "screenshots" folder and display it using:

![Calculator Output](screenshots/calculator-output.png)

How to Run

1. Clone the Repository

git clone https://github.com/hanigonuguntla19-ux/simple-calculator-python.git

2. Open the Project Directory

cd simple-calculator-python

3. Run the Application

python calculator.py

Requirements

This project uses only the Python standard library.

No external packages are required.

Python 3.8 or higher is recommended.

Future Enhancements

- Graphical User Interface
- Calculation history
- Scientific calculator operations
- Percentage calculations
- Memory functions
- Keyboard-based controls

Author

Hani Gonuguntla

GitHub: https://github.com/hanigonuguntla19-ux

License

This project is created for educational and portfolio purposes.
