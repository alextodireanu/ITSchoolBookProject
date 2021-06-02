import csv
from date_function import correct_date
import add_book_feature
from list_books_feature import list_books

fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]

# share book reader & writer
def share_book_reader_writer():
    shared_book = input("Which book would you like to share? -> ")
    shared_with = ""
    is_read = False
    updated_shared_list = []
    book_found = []
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                updated_shared_list.append(row)
                if row.get(fieldnames[0]) == shared_book.title().strip():
                    book_found.append(True)
                    updated_shared_list.remove(row)
                    # using condition to make a book shareable only if it's marked as read
                    if row.get(fieldnames[2]) != "True":
                        book_not_read = input("The selected book is not yet read. Did you finish it? Reply with Y/N -> ")
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
                            shared_with = input("With whom would you like to share the book? Type here -> ")
                            print(f"Book successfully shared with {shared_with.title().strip()}")
                        else:
                            raise TypeError("incorrect button pressed")
                    else:
                        is_read = True
                        start_date = row['StartDate']
                        end_date = row['EndDate']
                        if row.get(fieldnames[6]) != "None":
                            print(f"Book is already shared with {row['SharedWith']}")
                            # provided the option to insert additional people to share the book with
                            additional_share = input("Would you like to share it with somebody else? Reply with Y/N -> ")
                            if additional_share.upper().strip() == "Y":
                                additional_share = input("Type the name(s) here. If multiple, please use ',' to separate them -> ")
                                shared_with = additional_share.title().strip() + ',' + row.get(fieldnames[6])
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
        print()
        return
    else:
        print()

    try:
        # providing the option to add the book if it was not found in our list, linked with add book feature
        if True not in book_found:
            book_not_found = input("The book was not found. Would you like to add it? Reply with Y/N -> ")
            if book_not_found.upper().strip() == "Y":
                add_book_feature.add_book()
                return
            elif book_not_found.upper().strip() == "N":
                print("Book will not be added, returning to main menu...")
                print()
                return
            else:
                raise TypeError("incorrect button pressed")
    except TypeError:
        print("Incorrect button pressed, returning to main menu...")
        print()
        return
    else:
        print()

    try:
        with open("booksDB.csv", mode='w', newline='') as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            writer.writerow(updated_shared_list[0])
            writer.writerow({fieldnames[0]: row.get(fieldnames[0]),
                             fieldnames[1]: row.get(fieldnames[1]),
                             fieldnames[2]: is_read,
                             fieldnames[3]: start_date,
                             fieldnames[4]: end_date,
                             fieldnames[5]: row.get(fieldnames[5]),
                             fieldnames[6]: shared_with.title().strip()})
            writer.writerows(updated_shared_list[1:])
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
