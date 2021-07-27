import csv
from date_function import correct_date
from list_books_feature import list_books
import tools
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# book notes reader & writer
def book_notes_reader_writer():
    book_name = input("For which book would you like to leave a note/review? -> ")
    # created method in tools module that will return
    # empty variables which will take values from the conditional tests; is_read defined as False
    author_name, start_date, end_date, notes, shared_with, is_read = tools.Utils.variables()
    # created 2 empty lists, book_found will store either True or False if the book is found in our file
    # books_list will store the rows from our CSV file
    books_list = []
    book_found = []
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, delimiter=',', fieldnames=fieldnames)
            for row in reader:
                books_list.append(row)
                if row.get(fieldnames[0]) == book_name.title().strip():
                    books_list.remove(row)
                    book_found.append(True)
                    author_name = row.get(fieldnames[1])
                    shared_with = row.get(fieldnames[6])
                    if row.get(fieldnames[2]) != 'True':
                        book_not_read = input("The selected book is not read. Did you finish it? Reply with Y/N -> ")
                        if book_not_read.upper().strip() == "Y":
                            is_read = True
                            start_date, end_date = correct_date()
                            notes = input("Leave your note/review here (min 3, max 30 characters) -> ")
                            if len(notes.strip()) < 3:
                                print("Note/review too short, nothing updated")
                                readFile.close()
                                return
                            elif len(notes.strip()) > 30:
                                print("Note/review too long, nothing updated")
                                readFile.close()
                                return
                            else:
                                print("Note/review added successfully")
                        elif book_not_read.upper().strip() == "N":
                            print("You can't leave a note/review for an unfinished book, returning to main menu...")
                            readFile.close()
                            return
                        else:
                            raise TypeError("incorrect button pressed")
                    else:
                        is_read = True
                        start_date = row.get(fieldnames[3])
                        end_date = row.get(fieldnames[4])
                        if row.get(fieldnames[5]) != "N/A":
                            print(f"There is already a note/review for this book: {row['Notes']}")
                            notes = input("Do you want to leave an additional review? Reply with Y/N -> ")
                            if notes.upper().strip() == 'Y':
                                notes = input("Leave your note/review here (min 3, max 30 characters) -> ")
                                if len(notes.strip()) < 3:
                                    print("Note/review too short, nothing updated")
                                    readFile.close()
                                    return
                                elif len(notes.strip()) > 30:
                                    print("Note/review too long, nothing updated")
                                    readFile.close()
                                    return
                                else:
                                    print("Note/review added successfully")
                                    notes += '; ' + row['Notes']
                else:
                    book_found.append(False)
    except IOError:
        print("Error while reading file")
        readFile.close()
        return
    except TypeError:
        print("Incorrect button pressed")
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
            # all the remaining rows are written after the reviewed book
            writer.writerows(books_list[1:])
    except IOError:
        print("Error while writing file")
        writeFile.close()
        return
    else:
        print()


# book notes feature
def book_notes():
    # added condition to return to the main menu if the file is empty
    if list_books() is False:
        return
    book_notes_reader_writer()
