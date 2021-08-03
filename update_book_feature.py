import csv
import tools as tl
from date_function import CorrectDate
from list_books_feature import ListBooks
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


class UpdateBook:
    """Class to represent the update book feature"""
    @staticmethod
    def _reader(book_name, book_author):
        """Helper method to read the CSV file"""
        # created an empty list to which we add the data from the file, row by row
        books_list = []
        book_found = False

        try:
            with open("booksDB.csv", mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                for row in reader:
                    books_list.append(row)
                    if row.get(fieldnames[0]) != book_name.title().strip() and \
                            row.get(fieldnames[1]) != book_author.title().strip():
                        continue
                    elif row.get(fieldnames[0]) == book_name.title().strip() and \
                            row.get(fieldnames[1]) == book_author.title().strip():
                        books_list.remove(row)
                        book_found = True

                        is_read = row.get(fieldnames[2])
                        if is_read == 'True':
                            print("The book is already read, nothing to update! Returning to main menu...\n")
                            return False
                        else:
                            # validating the start and end dates using the correct_date method
                            dates = CorrectDate.correct_date()
                            if dates is False:
                                return False
                            else:
                                start_date, end_date = dates
                                is_read = True
                                shared_with = 'N/A'
                                notes = 'N/A'
                readFile.close()
                # checking if the book has been found in our file
                if book_found is False:
                    print("Book not found! Please select the ADD BOOK option from the main menu...\n")
                    return False

        # treating the exception where the file doesn't exist
        except IOError:
            tl.Utils.create_file()
            return False

        else:
            print("Dates successfully updated!\n")
            return books_list, book_name, book_author, is_read, start_date, end_date, shared_with, notes

    @staticmethod
    def _writer(book_name, book_author):
        """Method to write the book's start and end dates to the CSV file"""
        # checking if the _reader method was successful; if yes, unpacking the variables from data
        data = UpdateBook._reader(book_name, book_author)
        if data is False:
            return False
        books_list, book_name, book_author, is_read, start_date, end_date, shared_with, notes = data

        try:
            with open("booksDB.csv", mode='w', newline='') as writeFile:
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                # rewriting the rows in the CSV file, the headers are the first row
                writer.writerow(books_list[0])
                # the updated book details are the 2nd row
                writer.writerow({fieldnames[0]: book_name.title().strip(),
                                 fieldnames[1]: book_author.title().strip(),
                                 fieldnames[2]: is_read,
                                 fieldnames[3]: start_date,
                                 fieldnames[4]: end_date,
                                 fieldnames[5]: notes,
                                 fieldnames[6]: shared_with.title().strip()})
                # all the remaining rows are written after the reviewed book
                writer.writerows(books_list[1:])
                writeFile.close()

        except IOError:
            print("Error while writing the file!\n")
            return False
        else:
            return

    @staticmethod
    def update_book():
        """Method to run the update book feature"""
        # checking if the list_books method is succesful and returns data
        if ListBooks.list_books() is False:
            return
        # validating the book name and author using the method from the Utils class
        book_data = tl.Utils.book_and_author_name()
        if book_data is False:
            return
        else:
            book_name, book_author = book_data
        if UpdateBook._writer(book_name, book_author) is False:
            return
