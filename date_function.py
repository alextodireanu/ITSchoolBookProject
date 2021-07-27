import datetime
from datetime import date


# created function to gather the user's input and validate the start and end dates
def correct_date():
    correct_start_date = False
    correct_end_date = False
    start_date = ""
    end_date = ""
    max_tries = 3
    tries = 0
    while not correct_start_date:
        if tries < max_tries:
            try:
                start_date = input("Please enter the date you started it (Y/M/D) -> ")
                tries += 1
                # converting the user's input to date format
                start_year, start_month, start_day = map(int, start_date.split("/"))
                start_date = datetime.date(start_year, start_month, start_day)
                # comparing start date with current date
                if start_date <= date.today():
                    correct_start_date = True
                else:
                    correct_start_date = False
                    if tries == max_tries:
                        print("Incorrect start date! No more tries left, returning to main menu...")
                        print()
                        return False
                    # raised error for start date higher than current date
                    raise KeyError("start date higher than current date")

                while not correct_end_date and correct_start_date:
                    try:
                        end_date = input("Please enter the date you finished it (Y/M/D) -> ")
                        # converting the user's input to date format
                        end_year, end_month, end_day = map(int, end_date.split("/"))
                        end_date = datetime.date(end_year, end_month, end_day)
                        # comparing end date with current date and start date
                        if start_date <= end_date <= date.today():
                            correct_end_date = True
                        elif end_date > date.today():
                            correct_end_date = False
                            if tries == max_tries:
                                print("Incorrect end date! No more tries left, returning to main menu...")
                                print()
                                return False
                            # raised error for end date higher than current date
                            raise IndexError("end date must not be after current date")
                        elif end_date < start_date:
                            correct_end_date = False
                            if tries == max_tries:
                                print("Incorrect end date! No more tries left, returning to main menu...")
                                return False
                            # raised error for end date lower than start date
                            raise AttributeError("end date must be after start date")
                    # treating the exception when the user's input is not in a valid format
                    except ValueError:
                        if tries == max_tries:
                            print("Incorrect end date! No more tries left, returning to main menu...")
                            print()
                            return False
                        elif tries == 2:
                            print("Last try")
                        else:
                            print(f"Incorrect end date, please try again, you have {max_tries - tries} tries left")
                        tries += 1
                    # treating the exception when the end date is higher than the current date
                    except IndexError:
                        correct_end_date = False
                        if tries == 2:
                            print("Last try")
                        else:
                            print(f"End date must not be after the current date, you have {max_tries - tries} tries left")
                        tries += 1
                    # treating the exception when the end date is lower than the start date
                    except AttributeError:
                        correct_end_date = False
                        if tries == 2:
                            print("Last try")
                        else:
                            print(f"End date must not be before the start date, you have {max_tries - tries} tries left")
                        tries += 1
                    # if the end date is correct - breaking the loop
                    else:
                        break
                # comparing start date with the end date
                if start_date > end_date:
                    if tries == max_tries:
                        print("Start date must be before end date. No more tries left, returning to main menu...")
                        print()
                        return False
                    # raised error for start date higher than end date
                    raise TypeError("start date higher than end date")
            # treating the exception when the user's input is not in a valid format
            except ValueError:
                if tries == max_tries:
                    print("Incorrect start date! No more tries left, returning to main menu")
                    return False
                elif tries == 2:
                    print("Last try")
                else:
                    print(f"Incorrect start date, please try again, you have {max_tries - tries} tries left")
            # treating the exception when the start date is higher than the end date
            except TypeError:
                if tries == 2:
                    print("Last try")
                else:
                    print(f"Start date must be before end date, you have {max_tries - tries} tries left")
                correct_start_date = False
            # treating the exception when the start date is higher than the current date
            except KeyError:
                if tries == 2:
                    print("Last try")
                else:
                    print(f"Start date must not be after the current date, you have {max_tries - tries} tries left")
                correct_start_date = False
            # if both the end date and start date are correct - breaking the loop
            else:
                print("Correct dates")
                break
    return start_date, end_date
