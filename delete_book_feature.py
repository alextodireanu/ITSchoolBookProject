import csv
from list_books_feature import list_books

fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# delete book function
def delete_book():
    if list_books() is False:
        return
    updated_list = []
    book_found = []
    delete_record = input("Which book would you like to delete? -> ")
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            for row in reader:
                updated_list.append(row)
                if row[fieldnames[0]] == delete_record.title().strip():
                    book_found.append(True)
                    updated_list.remove(row)
                    print("Book deleted")
                else:
                    book_found.append(False)
        readFile.close()

        if True not in book_found:
            print("Book not found, returning to main menu...")
            print()
            return

        with open("booksDB.csv", mode='w', newline='') as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            writer.writerows(updated_list)
        writeFile.close()
    except IOError:
        print("Error updating file")
    else:
        print()
