import csv
import tools as tl
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


class ListBooks:
    """Class to represent the list books feature"""
    @staticmethod
    def _check_header():
        """Method to check if the headers exist"""
        try:
            with open("booksDB.csv", mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                # reading the 1st and 2nd rows from the CSV file
                if next(reader) is False:
                    raise StopIteration("headers don't exist")
                else:
                    if next(reader) is False:
                        raise StopIteration("2nd row is empty")
                # returning to the first position
                readFile.seek(0)
                readFile.close()

        # treating exception where the 1st row is empty
        except StopIteration:
            print("Warning! The file is empty, please add books!\n")
            return False

        else:
            pass

    @staticmethod
    def list_books():
        """Method to read the CSV file and print the books"""
        try:
            with open("booksDB.csv", mode='r', newline='') as readFile:
                reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
                if ListBooks._check_header() is False:
                    return False
                for row in reader:
                    print(f"{row['BookName']}, {row['AuthorName']}, {row['IsRead']}, {row['StartDate']}, "
                          f"{row['EndDate']}, {row['Notes']}, {row['SharedWith']}")
            readFile.close()

        # treating the exception where the file doesn't exist
        except IOError:
            tl.Utils.create_file()
            return False
        else:
            print('\n')
            return
