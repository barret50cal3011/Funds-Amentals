from datetime import datetime, timedelta

class Time:
    def __init__(self, start_date: str = "2024-01-01"):
        # Convert the start date from a string to a datetime object
        self.__current_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    def get_next_date(self):
        # Get the current date as a string in YYYY-MM-DD format
        date_str = self.__current_date.strftime("%Y-%m-%d")
        # Move the current date forward by one day
        self.__current_date += timedelta(days=1)
        return date_str
    def get_date(self):
        """
        The `get_date` function returns the current date stored in the `__current_date` attribute.
        :return: The method `get_date` is returning the value of the private attribute `__current_date`.
        """
        return self.__current_date
