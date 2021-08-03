import csv
from date_function import CorrectDate
import tools as tl
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# add book - reader & writer
class AddBook:
    """Class to represent the add book feature"""
    @staticmethod
    def _check_header():
        """Helper method to check if the headers exist in the CSV file"""
        try:
            with open('booksDB.csv', mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                # code to take a snippet from our CSV file and check if the headers exist
                if next(reader) is False:
                    readFile.seek(0)
                    raise StopIteration("headers don't exist")

        # treating the exception where the headers don't exist
        except StopIteration:
            with open('booksDB.csv', mode='w') as writeFile:
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                writer.writeheader()
                writeFile.close()

        else:
            pass

    @staticmethod
    def _reader(book_name, book_author):
        """Helper method to read the contents of the CSV file"""
        try:
            with open('booksDB.csv', mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                AddBook._check_header()
                for row in reader:
                    # checking if the book already exists in our file
                    if row.get(fieldnames[0]) == book_name.title().strip() and \
                            row.get(fieldnames[1]) == book_author.title().strip():
                        book_edit = input("Book already exists! "
                                          "Do you want to update it? Reply with Y/N -> ")
                        if book_edit.upper().strip() == "Y":
                            print("Returning to main menu, please choose the update book option...\n")
                            readFile.close()
                            return False
                        elif book_edit.upper().strip() == "N":
                            print("Book will not be updated!\n")
                            readFile.close()
                            return False
                        else:
                            raise tl.IncorrectKey("incorrect button pressed")

        # treating the exception where the file doesn't exist
        except IOError:
            tl.Utils.create_file()
        # treating the exception where the user presses an incorrect button
        except tl.IncorrectKey:
            print("Incorrect button pressed, returning to main menu...\n")
            return False

        else:
            readFile.close()
            pass

    @staticmethod
    def _additional_data():
        """Helper method to check if the book is read, shared and reviewed"""
        is_read = input("Did you read it? Reply with Y/N -> ")
        try:
            if is_read.upper().strip() == "Y":
                # validating the start and end dates using the correct_date method
                dates = CorrectDate.correct_date()
                if dates is False:
                    return False
                else:
                    start_date, end_date = dates

                notes = input("Would you like to leave a note? Reply with Y/N -> ")
                if notes.upper().strip() == "Y":
                    notes = input("Leave a short comment -> ")
                elif notes.upper().strip() == "N":
                    notes = "N/A"
                else:
                    raise tl.IncorrectKey('incorrect button pressed')

                is_shared = input("Do you want to share it with somebody? Reply with Y/N -> ")
                if is_shared.upper().strip() == "Y":
                    shared_with = input("With whom would you like to share it? -> ")
                    print("Book added and shared successfully! Returning to main menu...\n")
                elif is_shared.upper().strip() == "N":
                    shared_with = "N/A"
                    print("Book added successfully but will not be shared, returning to main menu...\n")
                else:
                    raise tl.IncorrectKey('incorrect button pressed')

            elif is_read.upper().strip() == "N":
                is_read = False
                start_date = "N/A"
                end_date = "N/A"
                notes = "N/A"
                shared_with = "N/A"
                print("Book added successfully! Returning to main menu...\n")
                return is_read, start_date, end_date, notes, shared_with

            else:
                raise tl.IncorrectKey("Incorrect button pressed")

        # treating the exception where the user presses an incorrect button
        except tl.IncorrectKey:
            print("Incorrect button pressed, returning to main menu...\n")
            return False

        else:
            is_read = True
            return is_read, start_date, end_date, notes, shared_with

    @staticmethod
    def _writer(book_name, book_author):
        """Helper method to write the book's details to the CSV file"""
        # checking if the _reader method is successful
        if AddBook._reader(book_name, book_author) is False:
            return False
        # checking if the _additional_data method is successful
        additional_data = AddBook._additional_data()
        if additional_data is False:
            return False
        else:
            is_read, start_date, end_date, notes, shared_with = additional_data

        # writing the data to the file
        try:
            with open('booksDB.csv', mode='a', newline='') as writeFile:
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                writer.writerow({fieldnames[0]: book_name.title().strip(),
                                 fieldnames[1]: book_author.title().strip(),
                                 fieldnames[2]: is_read,
                                 fieldnames[3]: start_date,
                                 fieldnames[4]: end_date,
                                 fieldnames[5]: notes.strip(),
                                 fieldnames[6]: shared_with.title().strip()})
                writeFile.close()

        except IOError:
            print("Error writing file\n")

        else:
            print('\n')
            return

    @staticmethod
    def add_book():
        """Method to run the add book feature"""
        # validating the book name and author using the method from the Utils class
        book_data = tl.Utils.book_and_author_name()
        if book_data is False:
            return
        else:
            book_name, author_name = book_data
        if AddBook._writer(book_name, author_name) is False:
            return
