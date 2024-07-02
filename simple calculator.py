def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1 , num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2
def calculator():
    print("Select operation:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")

    choice = input("Enter choice (1 or 2 or 3 or 4 ): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input, Please enter a valid choice.")

while True:
    calculator()
    again = input("Do you want to continue? (yes/no): ").lower()
    if again != 'yes':
        print("Exiting the calculator")
        break
