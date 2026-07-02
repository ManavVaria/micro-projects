print("Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = int(input("Enter choice (1/2/3/4/5): "))
if choice == 1:
    num1 = float(input("Enter first Number: "))
    num2 = float(input("Enter second Number: "))
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == 2:
    num1 = float(input("Enter first Number: "))
    num2 = float(input("Enter second Number: "))
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == 3:
    num1 = float(input("Enter first Number: "))
    num2 = float(input("Enter second Number: "))
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif choice == 4:
    num1 = float(input("Enter first Number: "))
    num2 = float(input("Enter second Number: "))
    result = num1 / num2
    print(num1, "/", num2, "=", result)
elif choice == 5:
    print("Exiting the calculator. Goodbye!")
else:
    choice = int(input("Invalid input. Please enter a valid choice (1/2/3/4/5): "))