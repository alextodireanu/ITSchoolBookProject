import csv
fieldnames = ["BookName", "AuthorName", "IsRead", "StartDate", "EndDate", "Notes", "SharedWith"]


# list books feature
def list_books():
    print()
    try:
        with open("booksDB.csv", mode='r', newline='') as readFile:
            reader = csv.DictReader(readFile, fieldnames=fieldnames, delimiter=',')
            try:
                # reading the 1st row from the CSV file
                if next(reader) is False:
                    raise StopIteration("1st row doesn't exist")
                else:
                    # reading the 2nd row from the CSV file
                    if next(reader) is False:
                        raise StopIteration("2nd row doesn't exist")
                # returning to the first position
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
