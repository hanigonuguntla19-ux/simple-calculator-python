print("----- Basic Calculator -----")
while True:
    print("\nChoose an operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Exit")

    option = input("Enter your option: ")

    if option == "5":
        print("Calculator closed.")
        break

    if option not in ["1", "2", "3", "4"]:
        print("Please enter a valid option.")
        continue

    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if option == "1":
        answer = first + second
        print("Answer:", answer)

    elif option == "2":
        answer = first - second
        print("Answer:", answer)

    elif option == "3":
        answer = first * second
        print("Answer:", answer)

    else:
        if second == 0:
            print("Division by zero is not possible.")
        else:
            answer = first / second
            print("Answer:", answer)
