import csv
from list_books_feature import ListBooks
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


class DeleteBook:
    """Class to represent the delete book feature"""
    @staticmethod
    def delete_book():
        """Method to delete a record from the CSV file"""
        # checking if the list_books method is succesful and returns data
        if ListBooks.list_books() is False:
            return
        # created an empty list to which we add the data from the file, row by row
        updated_list = []
        book_found = False
        delete_record = input("Which book would you like to delete? -> ")

        try:
            with open("booksDB.csv", mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                for row in reader:
                    updated_list.append(row)
                    if row[fieldnames[0]] != delete_record.title().strip():
                        continue
                    else:
                        updated_list.remove(row)
                        book_found = True
                readFile.close()

            # checking if the book has been found in our file
            if book_found is False:
                print("Book not found, returning to main menu...\n")
                return

            # clearing the file completely if the last book is deleted
            if len(updated_list) == 1:
                with open('booksDB.csv', mode='w+', newline='') as file:
                    file.close()
                    return
            # writing the data back to the file if we don't delete the only record
            else:
                with open("booksDB.csv", mode='w', newline='') as writeFile:
                    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                    writer.writerows(updated_list)
                    writeFile.close()

        except IOError:
            print("Error updating file\n")
            return

        else:
            print("Book deleted! Returning to main menu...\n")
            return
