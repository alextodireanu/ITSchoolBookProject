# importing the modules created for each feature
import add_book_feature
from list_books_feature import list_books
import update_book_feature
import share_book_feature
from clear_file_feature import clear_file
from delete_book_feature import delete_book
import book_notes_feature

# Main Menu function
def main_menu():
    options = ("Add a book", "List the existing books", "Update a book", "Share a book", "Leave a note", "Clear file", "Delete book", "Quit")
    index = 1
    print("Hello! Main menu:")
    print()
    for option in options:
        print(f"{index}.{option}")
        index += 1
    print()
    try:
        option = int(input("Please select an option -> "))
        if option == 1:
            add_book_feature.add_book()
        elif option == 2:
            list_books()
        elif option == 3:
            update_book_feature.update_book()
        elif option == 4:
            share_book_feature.share_book()
        elif option == 5:
            book_notes_feature.book_notes()
        elif option == 6:
            clear_file()
        elif option == 7:
            delete_book()
        elif option == 8:
            print("App closed, goodbye!")
        else:
            raise TypeError("incorrect option")
    except TypeError:
        print("Incorrect option selected")
        print()
    except ValueError:
        print("Only numbers from 1-8 are accepted")
        print()
    else:
        return option

# App start function
def appStart():
    max_tries = 3
    tries = 0
    start = input("Press * to start the app -> ")
    if start.strip() == "*":
        is_started = True
    else:
        tries += 1
        is_started = False

    while not is_started and tries < max_tries:
        if tries == 2:
            print("Last try, otherwise the app will close")
            start = input("Press * to start the app -> ")
            if start.strip() == "*":
                is_started = True
            else:
                print("App closed!")
        elif tries < 2:
            print(f"Incorrect button pressed, you have {max_tries - tries} tries left")
            start = input("Press * to start the app -> ")
            if start.strip() == "*":
                is_started = True
        tries += 1

    while is_started:
        option = main_menu()
        if option == 8:
            break

appStart()