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

def add_book():
    book_name = input("Insert the book title -> ")
    author_name = input("Insert the author name -> ")
    # importing os.path to check if the file already exists and avoid creating the headers with each entry in our CSV
    import csv, os.path
    file_exists = os.path.isfile('booksDB.csv')
    # mode = a, appends a new line with each entry at the end of the CSV file
    with open('booksDB.csv', mode='a', newline='') as file:
        fieldnames = ["BookName", "AuthorName", "SharedWith", "IsRead"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #  not writing the headers if the file already exists
        if not file_exists:
            writer.writeheader()
        writer.writerow({fieldnames[0]: book_name,
                        fieldnames[1]: author_name,
                        fieldnames[2]: 'None',
                        fieldnames[3]: False})
    print("Book has been added successfully")


def list_books():
    import csv
    with open('booksDB.csv', mode='r', newline='') as file:
        #  1: gather the data from the DB
        rows = csv.DictReader(file, delimiter=',')
        #  2: reading the file row by row and printing it like a table
        fieldnames = "BookName, AuthorName, SharedWith, IsRead"
        print(fieldnames)
        for row in rows:
            print(f"{row['BookName']}, {row['AuthorName']}, {row['SharedWith']}, {row['IsRead']}")


def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    if book_read.lower() == 'y':
        book_read = True
    else:
        book_read = False
    import csv
    rows = []
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                             "AuthorName": row.get("AuthorName"),
                             "SharedWith": row.get("SharedWith"),
                             "IsRead": book_read}
                            )
        print("Book was updated successfully")

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