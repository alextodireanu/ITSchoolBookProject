# clear file function
def clear_file():
    try:
        empty_file = input("This will delete all the records. Are you sure? Y/N -> ")
        if empty_file.upper().strip() == "Y":
            # deleting the records by truncating the file
            with open("booksDB.csv", mode='w+') as file:
                file.close()
            print("File cleared")
            print()
        elif empty_file.upper().strip() == "N":
            print("No changes made")
            print()
        else:
            raise TypeError("incorrect button pressed")
    # treating exception where the user presses an incorrect button
    except TypeError:
        print("Incorrect button pressed")
    # treating exception where the file cannot be written
    except IOError:
        print("Error clearing file")
    else:
        print()
