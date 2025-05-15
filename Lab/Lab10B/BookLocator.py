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

    keep_running = True
    # The loop below is purposely set to an infinite loop. There is logic
    # to exit the application if the user doesn't want to select any more books.
    while keep_running:
        call_number = get_input()

        if call_number is None:
            break

        location_of_book = find_book(call_number)

        display_result(location_of_book)

        # Invoke main to start application.
if __name__ == "__main__":
    main()
    # Function to determine the location of a book based on its call number
def find_book(call_number):
    if call_number < 100:
        return "Book not found!"
    elif 100 <= call_number <= 199:
        return "Basement"
    elif 200 <= call_number <= 500 or call_number > 900:
        return "Main Floor"
    elif (501 <= call_number <= 900) and not (700 <= call_number <= 750):
        return "Upper Floor"
    elif 700 <= call_number <= 750:
        return "Archives"