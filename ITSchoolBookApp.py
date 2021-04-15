def add_book():
    print("Add a book option selected")
def list_books():
    print("List the existing books option selected")
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