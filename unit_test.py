# Rules for locating books, defined outside the function
location_rules = [
    {"range": (0, 99), "location": "Book not found!"},
    {"range": (100, 199), "location": "Basement"},
    {"range": (200, 500), "location": "Main Floor"},
    {"range": (501, 699), "location": "Upper Floor"},
    {"range": (700, 750), "location": "Archives"},
    {"range": (751, 900), "location": "Upper Floor"},
    {"range": (901, float('inf')), "location": "Main Floor"},
]

# Function to find the book based on the call number
def find_book(call_number):
    for rule in location_rules:
        start, end = rule["range"]
        if start <= call_number <= end:
            return rule["location"]
    return "Book not found!"


# Message to use when exiting the application
def good_bye():
    print("Good-bye!")


# Function to retrieve information from the user.
def get_input():
    answer = input("Do you want to locate a book (yes/no)? ")

    # If user doesn't want to locate a book, exit the application.
    if answer.lower() == 'no':
        good_bye()
        return None

    if answer.lower() != 'yes':
        # Recursive call to itself to show the question again.
        return get_input()

    return int(input("\nEnter a call number: "))


# Display the result from the request.
def display_result(result):
    print(f"\n*** Location of your book: {result}", end="\n\n")


def main():
    print("{0:^40}".format("Welcome to QCC Book Locator"))
    print("=" * 40)

    while True:
        call_number = get_input()

        if call_number is None:
            break

        location_of_book = find_book(call_number)
        display_result(location_of_book)


# Invoke main to start application.
if __name__ == "__main__":
    main()
