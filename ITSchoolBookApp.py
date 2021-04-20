def add_book():
    book_name = input("Insert the book title -> ")
    author_name = input("Insert the author name -> ")
    #  importing CSV library
    import csv
    with open('booksDB.csv', mode='w') as file:
        fieldnames = ["BookName", "AuthorName", "SharedWith", "IsRead"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"BookName": book_name,
                        "AuthorName": author_name,
                        "SharedWith": 'None',
                        "IsRead": False})
    print("Book has been added successfully")


def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  1: gather the data from the DB
        rows = csv.DictReader(file)
        #  2: read the file row by row
        for row in rows:
            # fieldnames = ["BookName", "AuthorName", "SharedWith", "IsRead"]
            # print(fieldnames)
            print(f"""Book name: {row['BookName']}, author: {row['AuthorName']}, shared with: {row['SharedWith']}, the book is read: {row['IsRead']}""")
        #  make it look like a table


def edit_book():
    print("Edit a book option selected")


def share_book():
    print("Share a book option selected")


# Main menu for user
print("""Hello! Main menu:
1. Add a book
2. List the existing books
3. Edit a book
4. Share a book""")
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
