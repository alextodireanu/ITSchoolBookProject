import csv
import tools
from date_function import correct_date
from list_books_feature import list_books

fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# share book reader & writer
def share_book_reader_writer():
    book_name = input("Which book would you like to share? -> ")
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
                books_list.append(row)
                if row.get(fieldnames[0]) == book_name.title().strip():
                    book_found.append(True)
                    books_list.remove(row)
                    author_name = row.get(fieldnames[1])
                    notes = row.get(fieldnames[5])
                    # using condition to make a book shareable only if it's marked as read
                    if row.get(fieldnames[2]) != "True":
                        book_not_read = input("The selected book is not read. Did you finish it? Reply with Y/N -> ")
                        # providing the option to mark the book as read and linked to correct_date function
                        if book_not_read.upper().strip() == "Y":
                            is_read = True
                            start_date, end_date = correct_date()
                        elif book_not_read.upper().strip() == "N":
                            print("You need to finish the book before sharing it. Returning to main menu...")
                            print()
                            readFile.close()
                            return
                        if row.get(fieldnames[6]) == "None":
                            shared_with = input("With whom would you like to share the book? "
                                                "Type here -> ").title().strip()
                            # shared_with.title().strip()
                            print(f"Book successfully shared with {shared_with}")
                        else:
                            raise TypeError("incorrect button pressed")
                    else:
                        is_read = True
                        start_date = row['StartDate']
                        end_date = row['EndDate']
                        if row.get(fieldnames[6]) != "None":
                            print(f"Book is already shared with {row['SharedWith']}")
                            # provided the option to insert additional people to share the book with
                            additional_share = input("Would you like to share it with someone else? Reply with Y/N -> ")
                            if additional_share.upper().strip() == "Y":
                                additional_share = input("Type the name(s) here. "
                                                         "If multiple, use ',' to separate them -> ")
                                shared_with = [additional_share.title().strip() + ', ' + row.get(fieldnames[6])]
                                print(f"Book successfully shared with {shared_with}")
                            elif additional_share.upper().strip() == "N":
                                print("Book will not be shared with anyone else! Returning to main menu...")
                                print()
                                readFile.close()
                                return
                            else:
                                raise TypeError("incorrect button pressed")
                        else:
                            shared_with = input("Book is not shared yet. With whom would you like to share it? -> ")
                            print(f"Book successfully shared with {shared_with.title().strip()}")
                else:
                    book_found.append(False)
    except TypeError:
        print("Incorrect button pressed, returning to main menu...")
        readFile.close()
        return print()
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
                             fieldnames[6]: shared_with})
            # all the remaining rows are written after the shared book
            writer.writerows(books_list[1:])
            writeFile.close()
    except IOError:
        print("Error writing file")
    else:
        print()


# share book feature
def share_book():
    # added condition to return to the main menu if the file is empty
    if list_books() is False:
        return
    share_book_reader_writer()
