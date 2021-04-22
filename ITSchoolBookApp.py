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


def edit_book():
    print("Edit a book option selected")


def share_book():
    print("Share a book option selected")


# Main menu for user
options = ["Add a book", "List the existing books", "Edit a book", "Share a book"]
index = 1
print("Hello! Main menu:")
for option in options:
    print(f"{index}.{option}")
    index += 1
option = int(input("Please select an option -> "))

if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    edit_book()
elif option == 4:
    share_book()
else:
    print("Selected option is not available")
