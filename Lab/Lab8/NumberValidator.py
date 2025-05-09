print("** ENTER ONLY WHOLE NUMBERS **")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))


product = first_number * second_number

print(f"The product of both numbers is: {product}")

def get_whole_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Both numbers need to be whole numbers. Please try again.")

print("** ENTER ONLY WHOLE NUMBERS **")
first_number = get_whole_number("Enter first number: ")
second_number = get_whole_number("Enter second number: ")

product = first_number * second_number
print(f"The product of both numbers is: {product}")

# The code above does not allow me to enter letters like w or r because when I do it take me back and tell me to enter a whole number.