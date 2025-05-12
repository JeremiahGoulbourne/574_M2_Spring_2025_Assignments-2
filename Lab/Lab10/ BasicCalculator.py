import math
import operator

# Basic Math Calculator

# Named Constant
OPTION_EXIT = -1

# Global variable
menu_options = {
    "Addition": 1,
    "Subtraction": 2,
    "Multiplication": 3,
    "Division": 4,
    "Square Root": 5,
    "Power": 6
}

def menu():
    # Local variable
    selection = 0

    # Keep looping while the selection is not one of the options.
    while selection not in menu_options.values() and selection != OPTION_EXIT:

        for option in menu_options:
            print(f"{menu_options[option]} {option}")

        print("\n(Enter -1 to exit application)\n")

        selection = eval(input("Please select an option from the menu above: "))

    return selection

def main():
    option = menu()

    print("\nHave a great day!")

# Only run the main function if this is the entry point for the application.
if __name__ == "__main__":
    main()