import csv
from date_function import correct_date
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# add book - reader & writer
def add_book_reader_writer():
    book_name = input("Please enter the book's name -> ")
    if len(book_name.strip()) < 3:
        print("Book name needs to have at least 3 characters. Returning to main menu...")
        return
    book_author = input("Please enter the book's author -> ")
    if len(book_author.strip()) < 3:
        print("Book author needs to have at least 3 characters. Returning to main menu...")
        return
    try:
        with open('booksDB.csv', mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            # code to take a snippet from our CSV file and check if the header exists
            try:
                # reading the first row to check if the headers exist
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
                print()
            for row in reader:
                # checking if the book already exists in our DB
                if row.get(fieldnames[0]) == book_name.title().strip():
                    book_edit = input("Book already exists. "
                                      "Do you want to return to the main menu and edit it? Reply with Y/N -> ")
                    if book_edit.upper().strip() == "Y":
                        print()
                        readFile.close()
                        return
                    elif book_edit.upper().strip() == "N":
                        print("Book will not be updated, returning to main menu...")
                        print()
                        readFile.close()
                        return
                    else:
                        raise TypeError("incorrect button pressed")
    except IOError:
        print("Error reading file")
    except TypeError:
        print("Incorrect button pressed, returning to main menu...")
    else:
        print("File read successfully")
        readFile.close()

    is_read = input("Did you read it? Reply with Y/N -> ")
    try:
        if is_read.upper().strip() == "Y":
            is_read = True
            start_date, end_date = correct_date()
            notes = input("Would you like to leave a note? Reply with Y/N -> ")
            if notes.upper().strip() == "Y":
                notes = input("Leave a short comment -> ")
            else:
                notes = "None"
            is_shared = input("Do you want to share it with somebody? Reply with Y/N -> ")
            if is_shared.upper().strip() == "Y":
                shared_with = input("With whom would you like to share it? -> ")
                print("Book added and shared successfully! Returning to main menu...")
                print()
            else:
                shared_with = "None"
                print("Book added successfully but will not be shared, returning to main menu...")
                print()
        elif is_read.upper().strip() == "N":
            is_read = False
            start_date = "N/A"
            end_date = "N/A"
            notes = "N/A"
            shared_with = "None"
            print("Book added successfully! Returning to main menu...")
            print()
        else:
            raise TypeError("Incorrect button pressed")
    # treating the exception where the user presses an incorrect button
    except TypeError:
        if is_read:
            return
        print("Incorrect button pressed, returning to main menu...")
        print()
        return
    else:
        print()

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
    except IOError:
        print("Error writing file")
    else:
        print()
        writeFile.close()


# add book feature
def add_book():
    print()
    add_book_reader_writer()
