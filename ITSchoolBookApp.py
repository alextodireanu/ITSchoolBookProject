# importing the CSV and datetime libraries
import csv
import datetime
from datetime import date

# defining the fieldnames for our CSV file
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# created function to gather the user's input and validate the start and end dates
def correct_date():
    correct_start_date = False
    correct_end_date = False
    start_date = ""
    end_date = ""
    max_tries = 3
    tries = 0
    while not correct_start_date:
        if tries < max_tries:
            try:
                start_date = input("Please enter the date you started it (Y/M/D) -> ")
                tries += 1
                # converting the user's input to date format
                start_year, start_month, start_day = map(int, start_date.split("/"))
                start_date = datetime.date(start_year, start_month, start_day)
                # comparing start date with current date
                if start_date <= date.today():
                    correct_start_date = True
                else:
                    correct_start_date = False
                    if tries == max_tries:
                        print("Incorrect start date! No more tries left, returning to main menu...")
                        print()
                        return False
                    # raised error for start date higher than current date
                    raise KeyError("start date higher than current date")

                while not correct_end_date and correct_start_date:
                    try:
                        end_date = input("Please enter the date you finished it (Y/M/D) -> ")
                        # converting the user's input to date format
                        end_year, end_month, end_day = map(int, end_date.split("/"))
                        end_date = datetime.date(end_year, end_month, end_day)
                        # comparing end date with current date and start date
                        if end_date <= date.today() and end_date >= start_date:
                            correct_end_date = True
                        elif end_date > date.today():
                            correct_end_date = False
                            if tries == max_tries:
                                print("Incorrect end date! No more tries left, returning to main menu...")
                                print()
                                return False
                            # raised error for end date higher than current date
                            raise IndexError("end date must not be after current date")
                        elif end_date < start_date:
                            correct_end_date = False
                            if tries == max_tries:
                                print("Incorrect end date! No more tries left, returning to main menu...")
                                return False
                            # raised error for end date lower than start date
                            raise AttributeError("end date must be after start date")
                    # treating the exception when the user's input is not in a valid format
                    except ValueError:
                        if tries == max_tries:
                            print("Incorrect end date! No more tries left, returning to main menu...")
                            print()
                            return False
                        elif tries == 2:
                            print("Last try")
                        else:
                            print(f"Incorrect end date, please try again, you have {max_tries - tries} tries left")
                        tries += 1
                    # treating the exception when the end date is higher than the current date
                    except IndexError:
                        correct_end_date = False
                        if tries == 2:
                            print("Last try")
                        else:
                            print(f"End date must not be after the current date, you have {max_tries - tries} tries left")
                        tries += 1
                    # treating the exception when the end date is lower than the start date
                    except AttributeError:
                        correct_end_date = False
                        if tries == 2:
                            print("Last try")
                        else:
                            print(f"End date must not be before the start date, you have {max_tries - tries} tries left")
                        tries += 1
                    # if the end date is correct - breaking the loop
                    else:
                        break
                # comparing start date with the end date
                if start_date > end_date:
                    if tries == max_tries:
                        print("Start date must be before end date. No more tries left, returning to main menu...")
                        print()
                        return False
                    # raised error for start date higher than end date
                    raise TypeError("start date higher than end date")
            # treating the exception when the user's input is not in a valid format
            except ValueError:
                if tries == max_tries:
                    print("Incorrect start date! No more tries left, returning to main menu")
                    return False
                elif tries == 2:
                    print("Last try")
                else:
                    print(f"Incorrect start date, please try again, you have {max_tries - tries} tries left")
            # treating the exception when the start date is higher than the end date
            except TypeError:
                if tries == 2:
                    print("Last try")
                else:
                    print(f"Start date must be before end date, you have {max_tries - tries} tries left")
                correct_start_date = False
            # treating the exception when the start date is higher than the current date
            except KeyError:
                if tries == 2:
                    print("Last try")
                else:
                    print(f"Start date must not be after the current date, you have {max_tries - tries} tries left")
                correct_start_date = False
            # if both the end date and start date are correct - breaking the loop
            else:
                print("Correct dates")
                break
    return start_date, end_date


# add book - reader & writer
def add_book_reader_writer():
    book_name = input("Please enter the book's name -> ")
    if len(book_name) < 3:
        print("Book name needs to have at least 3 characters. Returning to main menu...")
        return
    book_author = input("Please enter the book's author -> ")
    if len(book_author) < 3:
        print("Book author needs to have at least 3 characters. Returning to main menu...")
        return
    try:
        with open('booksDB.csv', mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            # code to take a snippet from our CSV file and check if the header exists
            try:
                test_bytes = readFile.read(1024)
                readFile.seek(0)
                has_header = csv.Sniffer().has_header(test_bytes)
            # treating the exception where the headers don't exist
            except _csv.Error:
                with open('booksDB.csv', mode='w') as writeFile:
                    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                    writer.writeheader()
                writeFile.close()
            else:
                print()
            for row in reader:
                # checking if the book already exists in our DB
                if row.get(fieldnames[0]) == book_name.title():
                    book_edit = input("Book already exists. Do you want to return to the main menu and edit it? Reply with Y/N -> ")
                    if book_edit.upper() == "Y":
                        print()
                        readFile.close()
                        return
                    elif book_edit.upper() == "N":
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
        if is_read.upper() == "Y":
            is_read = True
            start_date, end_date = correct_date()
            notes = input("Would you like to leave a note? Reply with Y/N -> ")
            if notes.upper() == "Y":
                comment = input("Leave a short comment -> ")
            else:
                comment = "None"
            is_shared = input("Do you want to share it with somebody? Reply with Y/N -> ")
            if is_shared.upper() == "Y":
                share_with = input("With whom would you like to share it? -> ")
                print("Book added and shared successfully! Returning to main menu...")
                print()
            else:
                share_with = "None"
                print("Book added successfully but will not be shared, returning to main menu...")
                print()
        elif is_read.upper() == "N":
            is_read = False
            start_date = "N/A"
            end_date = "N/A"
            comment = "N/A"
            share_with = "None"
            print("Book added successfully! Returning to main menu...")
            print()
        else:
            raise TypeError("Incorrect button pressed")
    # treating the exception where the user doesn't press Y or N
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
            writer.writerow({fieldnames[0]: book_name.title(),
                             fieldnames[1]: book_author.title(),
                             fieldnames[2]: is_read,
                             fieldnames[3]: start_date,
                             fieldnames[4]: end_date,
                             fieldnames[5]: comment,
                             fieldnames[6]: share_with.title()})
    except IOError:
        print("Error writing file")
    else:
        print()
        writeFile.close()


# add book feature
def add_book():
    print()
    add_book_reader_writer()


# list books feature
def list_books():
    print()
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            try:
                if next(reader) is False:
                    raise StopIteration("1st row doesn't exist")
                else:
                    if next(reader) is False:
                        raise StopIteration("2nd row doesn't exist")
                readFile.seek(0)
                # treating exception where the 1st or 2nd row doesn't exist
            except StopIteration:
                print("Warning! The file is empty, please add books!")
                print()
                readFile.close()
                return False
            else:
                print()
            for row in reader:
                print(f"{row['BookName']}, {row['AuthorName']}, {row['IsRead']}, {row['StartDate']}, {row['EndDate']}, {row['Notes']}, {row['SharedWith']}")
        readFile.close()
    except IOError:
        print("Error reading file")
    else:
        print()


# update book feature
def update_book():
    # added condition to return to the main menu if the file is empty
    if list_books() is False:
        return
    update_book_reader_writer()


def share_book():
    book_name = input("Type the name of the book you want to share -> ")
    share_with = input("With whom would you like to share it? -> ")
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["SharedWith"] = share_with
                break
            else:
                print("Book is not in DB")
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                             "AuthorName": row.get("AuthorName"),
                             "SharedWith": share_with,
                             "IsRead": row.get("IsRead")}
                            )
        print(f"Book has been shared with {share_with} successfully")


# Main Menu function
def main_menu():
    options = ("Add a book", "List the existing books", "Update a book", "Share a book", "Leave a note", "Clear file", "Delete book", "Quit")
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
            add_book()
        elif option == 2:
            list_books()
        elif option == 3:
            update_book()
        elif option == 4:
            share_book()
        elif option == 5:
            book_notes()
        elif option == 6:
            clear_file()
        elif option == 7:
            delete_book()
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

# App start function
def appStart():
    max_tries = 3
    tries = 0
    start = input("Press * to start the app -> ")
    if start == "*":
        is_started = True
    else:
        tries += 1
        is_started = False

    while not is_started and tries < max_tries:
        if tries == 2:
            print("Last try, otherwise the app will close")
            start = input("Press * to start the app -> ")
            if start == "*":
                is_started = True
            else:
                print("App closed!")
        elif tries < 2:
            print(f"Incorrect button pressed, you have {max_tries - tries} tries left")
            start = input("Press * to start the app -> ")
            if start == "*":
                is_started = True
        tries += 1

    while is_started:
        option = main_menu()
        if option == 8:
            break

appStart()