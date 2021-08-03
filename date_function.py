import datetime
from datetime import date
import tools as tl


class CorrectDate:
    """Class to represent the method that gathers and validates the dates from the user"""
    @staticmethod
    def _validate_start_date():
        """Method to gather and validate the start date"""
        correct_start_date = False
        max_tries = 3
        tries = 0

        while not correct_start_date:
            if tries < max_tries:
                try:
                    start_date = input("Please enter the date you started it (Y/M/D) -> ")
                    tries += 1

                    # validating the date format
                    start_date = start_date.split('/')
                    if len(start_date[0]) != 4 or len(start_date[1]) > 2 or len(start_date[2]) > 2:
                        raise tl.IncorrectDateFormat

                    # converting the user's input to date format
                    start_year, start_month, start_day = map(int, start_date)
                    start_date = datetime.date(start_year, start_month, start_day)

                    # comparing start date with current date
                    if start_date <= date.today():
                        return start_date
                    else:
                        # raised error for start date higher than current date
                        raise tl.IncorrectStartDate("start date higher than current date")

                # treating the exception where the start date is incorrect, i.e. day is 32, or month 13
                except ValueError:
                    if tries == max_tries:
                        print("Incorrect start date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f"Incorrect start date, you have {max_tries - tries} tries left")

                # treating the exception where the start date is higher than the current date
                except tl.IncorrectStartDate:
                    if tries == max_tries:
                        print("Incorrect start date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f"Start date must not be after the current date, you have {max_tries - tries} tries left")

                # treating the exception where the date has an incorrect format
                except tl.IncorrectDateFormat:
                    if tries == max_tries:
                        print("Incorrect start date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f'Incorrect format, you have {max_tries - tries} tries left!')

    @staticmethod
    def _validate_end_date():
        """Method to gather and validate the end date"""
        correct_end_date = False
        max_tries = 3
        tries = 0

        while not correct_end_date:
            if tries < max_tries:
                try:
                    end_date = input("Please enter the date you finished it (Y/M/D) -> ")
                    tries += 1
                    # validating the date format
                    end_date = end_date.split('/')
                    if len(end_date[0]) != 4 or len(end_date[1]) > 2 or len(end_date[2]) > 2:
                        raise tl.IncorrectDateFormat

                    # converting the user's input to date format
                    end_year, end_month, end_day = map(int, end_date)
                    end_date = datetime.date(end_year, end_month, end_day)

                    # comparing end date with current date
                    if end_date <= date.today():
                        return end_date
                    else:
                        # raised error for end date higher than current date
                        raise tl.IncorrectEndDate("end date higher than current date")

                # treating the exception where the end date is incorrect, i.e. day is 32, or month 13
                except ValueError:
                    if tries == max_tries:
                        print("Incorrect end date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f"Incorrect end date, you have {max_tries - tries} tries left")

                # treating the exception where the start date is higher than the current date
                except tl.IncorrectEndDate:
                    if tries == max_tries:
                        print("Incorrect end date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f"End date must not be after the current date, you have {max_tries - tries} tries left")

                # treating the exception where the date has an incorrect format
                except tl.IncorrectDateFormat:
                    if tries == max_tries:
                        print("Incorrect end date! No more tries left, returning to main menu...\n")
                        return False
                    elif tries == 2:
                        print("Last try!")
                    else:
                        print(f'Incorrect format, you have {max_tries - tries} tries left!')

    @staticmethod
    def correct_date():
        """Method to validate the start date and end date"""
        start_date = CorrectDate._validate_start_date()
        if start_date is False:
            return
        end_date = CorrectDate._validate_end_date()
        if end_date is False:
            return
        if start_date <= end_date:
            return start_date, end_date
        else:
            print('Start date cannot be after the end date, returning to main menu...\n')
            return False
