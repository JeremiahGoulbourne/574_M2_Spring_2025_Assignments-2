## Find the minimum, maximum, and average of a sequence of numbers.
# Obtain list of numbers.
list1 = []
print("Requirements: ")
print("-- Enter -1 to terminate entering numbers.")
print("-- You have to enter 3, or more, nonnegative numbers.")

num = eval(input("Enter a number: "))

# Loop to retrieve remaining numbers with input validation
while num != -1:
    if num < 0:
        print("Sorry, invalid number entered. Numbers must be nonnegative values.")
    else:
        list1.append(num)
    num = eval(input("Enter another number: "))

# Initialize list for numbers
list1 = []

print("Requirements:")
print("- Enter -1 to terminate entering numbers.")
print("- You have to enter 3, or more, nonnegative numbers.")

# Obtain first number
num = eval(input("Enter a number: "))

# Loop to retrieve remaining numbers with input validation
while num != -1:
    if num < 0:
        print("Sorry, invalid number entered. Numbers must be nonnegative values.")
    else:
        list1.append(num)
    num = eval(input("Enter another number: "))

# Conditional structure to determine output
if len(list1) == 0:
    print("\nYou ended the application early. Good-bye!")
elif len(list1) < 3:
    print("\nSorry, you didn't enter the required nonnegative numbers for processing.")
else:
    print("\nResults:")
    print(f"Lowest number: {min(list1)}")
    print(f"Highest number: {max(list1)}")
    print(f"Average: {sum(list1) / len(list1):.2f}")
    print(f"Sorted numbers: {sorted(list1)}")
