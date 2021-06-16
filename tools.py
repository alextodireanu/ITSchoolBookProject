# importing the modules for our features
import add_book_feature
import list_books_feature
import update_book_feature
import share_book_feature
import book_notes_feature
import clear_file_feature
import delete_book_feature
import os
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# created Utils class which contains the following methods: main menu, app start and find book
class Utils:
    @ staticmethod
    def clear_screen():
        os.system('cls')

    @ staticmethod
    def main_menu():
        options = ("Add a book", "List the existing books", "Update a book", "Share a book",
                   "Leave a note", "Clear file", "Delete book", "Quit")
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
                Utils.clear_screen()
                add_book_feature.add_book()
            elif option == 2:
                list_books_feature.list_books()
            elif option == 3:
                Utils.clear_screen()
                update_book_feature.update_book()
            elif option == 4:
                Utils.clear_screen()
                share_book_feature.share_book()
            elif option == 5:
                Utils.clear_screen()
                book_notes_feature.book_notes()
            elif option == 6:
                Utils.clear_screen()
                clear_file_feature.clear_file()
            elif option == 7:
                Utils.clear_screen()
                delete_book_feature.delete_book()
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

    @staticmethod
    def app_start():
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
    def find_book():
        try:
            add_new_book = input("Book not found! Do you want to add it? Reply with Y/N -> ")
            if add_new_book.upper().strip() == "Y":
                add_book_feature.add_book()
            elif add_new_book.upper().strip() == "N":
                print("Returning to main menu...")
                return print()
            else:
                raise TypeError("incorrect button pressed")
        except TypeError:
            print("Incorrect button pressed, returning to main menu...")
            return print()
        else:
            return print()

    @staticmethod
    def variables():
        author_name = ""
        start_date = ""
        end_date = ""
        notes = ""
        shared_with = ""
        is_read = False
        return [author_name, start_date, end_date, notes, shared_with, is_read]
