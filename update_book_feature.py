import csv
from date_function import correct_date
import add_book_feature
from list_books_feature import list_books

fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# update book - reader & writer
def update_book_reader_writer():
    # defining start and end date as empty and they will take values from the correct_date function
    start_date = ""
    end_date = ""
    is_read = False
    # created 2 empty lists, book_found will store either True or False if the book is found in our file
    # updated_list will store the rows from our CSV file
    book_found = []
    updated_list = []
    updated_book = input("Please type the title of the book you want to edit -> ")
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                # we read the file row by row and add it to updated_list
                updated_list.append(row)
                # if the book is found, we delete the row from updated_list and add True to book_found
                if row.get(fieldnames[0]) == updated_book.title().strip():
                    book_found.append(True)
                    updated_list.remove(row)
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
                            print()
                            return
                        else:
                            raise TypeError("Incorrect button pressed")
                    # if the book is already read, returning to main menu as there's nothing to update
                    else:
                        print("Book is already read, nothing to update, returning to main menu...")
                        return
                # adding False to book_found if the book is not in our file after all the rows have been read
                else:
                    book_found.append(False)
            readFile.close()
    except IOError:
        print("Error reading file")
    except TypeError:
        if is_read:
            return
        print("Incorrect button pressed, returning to main menu...")
        return
    else:
        print()

    try:
        # checking if the book that needs to be edited is in our CSV file by looking for True value in book_found list
        if True not in book_found:
            # giving the option to add the book if it's not in our DB
            book_not_found = input("Book not found! Would you like to add it? Reply with Y/N -> ")
            if book_not_found.upper().strip() == "Y":
                readFile.close()
                add_book_feature.add_book()
                return
            elif book_not_found.upper().strip() == "N":
                readFile.close()
                print("Nothing to update, returning to main menu...")
                print()
                return
            else:
                raise TypeError("Incorrect button pressed")
    except TypeError:
        print("Incorrect button pressed, returning to main menu...")
        return

    try:
        with open("booksDB.csv", mode='w', newline='') as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            # rewriting the rows in the CSV file, the headers are the first row
            writer.writerow(updated_list[0])
            # the updated book details are the 2nd row
            writer.writerow({fieldnames[0]: row.get(fieldnames[0]),
                             fieldnames[1]: row.get(fieldnames[1]),
                             fieldnames[2]: is_read,
                             fieldnames[3]: start_date,
                             fieldnames[4]: end_date,
                             fieldnames[5]: row.get(fieldnames[5]),
                             fieldnames[6]: row.get(fieldnames[6])})
            # all the remaining rows are written after the updated book
            writer.writerows(updated_list[1:])
            writeFile.close()
    except IOError:
        print("Error while writing file")
    else:
        print()


# update book feature
def update_book():
    # added condition to return to the main menu if the file is empty
    if list_books() is False:
        return
    update_book_reader_writer()
