import csv
import tools
from date_function import correct_date
from list_books_feature import list_books
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# update book - reader & writer
def update_book_reader_writer():
    book_name = input("Please type the title of the book you want to edit -> ")
    # created method in tools module that will return
    # empty variables which will take values from the conditional tests; is_read defined as False
    author_name, start_date, end_date, notes, shared_with, is_read = tools.Utils.variables()
    # created 2 empty lists, book_found will store either True or False if the book is found in our file
    # books_list will store the rows from our CSV file
    books_list = []
    book_found = []
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                # we read the file row by row and add it to updated_list
                books_list.append(row)
                # if the book is found, we delete the row from updated_list and add True to book_found
                if row.get(fieldnames[0]) == book_name.title().strip():
                    book_found.append(True)
                    books_list.remove(row)
                    author_name = row.get(fieldnames[1])
                    notes = row.get(fieldnames[5])
                    shared_with = row.get(fieldnames[6])
                    # making the edit option available only if the book is read
                    if row.get(fieldnames[2]) != "True":
                        book_finished = input("Did you finish the book? Reply with Y/N -> ")
                        if book_finished.upper().strip() == "Y":
                            is_read = True
                            start_date, end_date = correct_date()
                            print("Book updated successfully! Returning to main menu...")
                            print()
                        elif book_finished.upper().strip() == "N":
                            is_read = False
                            print("You cannot edit an unfinished book, returning to main menu")
                            readFile.close()
                            return print()
                        else:
                            raise TypeError("Incorrect button pressed")
                    # if the book is already read, returning to main menu as there's nothing to update
                    else:
                        print("Book is already read, nothing to update, returning to main menu...")
                        readFile.close()
                        return
                # adding False to book_found if the book is not in our file after all the rows have been read
                else:
                    book_found.append(False)
    except IOError:
        print("Error reading file")
        readFile.close()
    except TypeError:
        # if is_read:
        #     return
        print("Incorrect button pressed, returning to main menu...")
        readFile.close()
        return
    else:
        readFile.close()
        print()

    # used the imported method from Utils class to search in our list
    if True not in book_found:
        tools.Utils.find_book()
        return

    try:
        with open("booksDB.csv", mode='w', newline='') as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            # rewriting the rows in the CSV file, the headers are the first row
            writer.writerow(books_list[0])
            # the updated book details are the 2nd row
            writer.writerow({fieldnames[0]: book_name.title(),
                             fieldnames[1]: author_name,
                             fieldnames[2]: is_read,
                             fieldnames[3]: start_date,
                             fieldnames[4]: end_date,
                             fieldnames[5]: notes,
                             fieldnames[6]: shared_with.title()})
            # all the remaining rows are written after the updated book
            writer.writerows(books_list[1:])
            writeFile.close()
    except IOError:
        print("Error while writing file")
        writeFile.close()
    else:
        print()


# update book feature
def update_book():
    # added condition to return to the main menu if the file is empty
    if list_books() is False:
        return
    update_book_reader_writer()
