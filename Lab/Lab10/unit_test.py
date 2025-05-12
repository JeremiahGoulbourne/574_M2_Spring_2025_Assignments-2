import operator
import math

# Constants
OPTION_EXIT = -1

# Function definitions
def addition(arg1, arg2):
    return operator.add(arg1, arg2)

def subtraction(arg1, arg2):
    return operator.sub(arg1, arg2)

def multiplication(arg1, arg2):
    return operator.mul(arg1, arg2)

def division(arg1, arg2):
    return operator.truediv(arg1, arg2)

def square_root(arg1, arg2):  # Using only the first argument
    return math.sqrt(arg1)

def power(arg1, arg2):
    return math.pow(arg1, arg2)

# Menu function
def menu():
    print("\n1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Square Root")
    print("6) Power")
    print("\n(Enter -1 to exit application)")
    try:
        return int(input("Please select an option from the menu above: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return menu()

# Main program
def main():
    option = menu()

    while option != OPTION_EXIT:
        try:
            num1 = float(input("Enter your first number: "))
            if option != 5:  # For all operations except square root
                num2 = float(input("Enter your second number: "))
            else:
                num2 = 0  # Placeholder for square_root

            if option == 1:
                result = addition(num1, num2)
                print(f"num1 + num2 = {result}")
            elif option == 2:
                result = subtraction(num1, num2)
                print(f"num1 - num2 = {result}")
            elif option == 3:
                result = multiplication(num1, num2)
                print(f"num1 * num2 = {result}")
            elif option == 4:
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = division(num1, num2)
                    print(f"num1 / num2 = {result}")
            elif option == 5:
                result = square_root(num1, num2)
                print(f"√num1 = {result}")
            elif option == 6:
                result = power(num1, num2)
                print(f"num1 ^ num2 = {result}")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

        option = menu()

    print("Have a great day!")

# Run the program
if __name__ == "__main__":
    main()
