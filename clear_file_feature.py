from list_books_feature import ListBooks
import tools as tl


class ClearFile:
    """Class to represent the clear file feature"""
    @staticmethod
    def clear_file():
        """Method to delete all the records from the CSV file"""
        # checking if the list_books method is succesful and returns data
        if ListBooks.list_books() is False:
            return
        try:
            empty_file = input("This will delete all the records. Are you sure? Y/N -> ")
            if empty_file.upper().strip() == "Y":
                # deleting the records by truncating the file
                with open("booksDB.csv", mode='w+') as file:
                    file.close()
                print("File cleared\n")
            elif empty_file.upper().strip() == "N":
                print("No changes made\n")
            else:
                raise tl.IncorrectKey("incorrect button pressed")

        # treating exception where the user presses an incorrect button
        except tl.IncorrectKey:
            print("Incorrect button pressed, returning to main menu...\n")
            return

        else:
            print('\n')
            return
