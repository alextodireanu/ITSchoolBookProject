from add_book_feature import AddBook
from list_books_feature import ListBooks
from update_book_feature import UpdateBook
from share_book_feature import ShareBook
from book_notes_feature import BookReview
from clear_file_feature import ClearFile
from delete_book_feature import DeleteBook
from os import path
import csv
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


class Utils:
    """Class to represent the methods that are used to run the app"""
    @staticmethod
    def book_and_author_name():
        """Method to validate the book's and author's name"""
        book_name = input("Please enter the book's name -> ")
        if len(book_name.strip()) < 3:
            print("Book name needs to have at least 3 characters. Returning to main menu...\n")
            return False
        book_author = input("Please enter the book's author -> ")
        if len(book_author.strip()) < 3:
            print("Book author needs to have at least 3 characters. Returning to main menu...\n")
            return False
        return book_name, book_author

    @staticmethod
    def main_menu():
        """Method used to run the main menu"""
        options = ("Add a book", "List the existing books", "Update a book", "Share a book",
                   "Leave a note", "Clear file", "Delete book", "Quit")
        index = 1
        print("Hello! Main menu:\n")
        for option in options:
            print(f"{index}.{option}")
            index += 1
        print()
        try:
            option = int(input("Please select an option -> "))
            if option == 1:
                AddBook.add_book()
            elif option == 2:
                ListBooks.list_books()
            elif option == 3:
                UpdateBook.update_book()
            elif option == 4:
                ShareBook.share_book()
            elif option == 5:
                BookReview.book_review()
            elif option == 6:
                try:
                    if path.exists('booksDB.csv'):
                        ClearFile.clear_file()
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    print('File not found! Please select options 1-5 to create the file, returning to main menu...\n')
                else:
                    pass
            elif option == 7:
                try:
                    if path.exists('booksDB.csv'):
                        DeleteBook.delete_book()
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    print('File not found! Please select options 1-5 to create the file, returning to main menu...\n')
                else:
                    pass
            elif option == 8:
                print("App closed, goodbye!")
            else:
                raise KeyError("incorrect option")
        except KeyError:
            print("Incorrect option selected!\n")
        except ValueError:
            print("Only numbers from 1-8 are accepted!\n")
        else:
            return option

    @staticmethod
    def app_start():
        """Method used to start the app"""
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
            option = Utils.main_menu()
            if option == 8:
                break

    @staticmethod
    def create_file():
        """Method to create the CSV file if it doesn't exist"""
        with open("booksDB.csv", mode='w', newline='') as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            writer.writeheader()
            writeFile.close()
        print('File successfully created!\n')


class IncorrectKey(Exception):
    """Class to create the IncorrectKey exception raised when a user presses an incorrect button"""
    pass


class IncorrectStartDate(Exception):
    """Class to create the IncorrectStartDate exception"""
    pass


class IncorrectDateFormat(Exception):
    """Class to create the IncorrectDateFormat exception"""


class IncorrectEndDate(Exception):
    """Class to create the IncorrectEndDate exception"""
    pass
