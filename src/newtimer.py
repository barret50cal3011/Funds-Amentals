from datetime import datetime, timedelta

class Time:
    def __init__(self, start_date: str = "2024-01-01"):
        # Convert the start date from a string to a datetime object
        self.current_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    def get_next_date(self):
        # Get the current date as a string in YYYY-MM-DD format
        date_str = self.current_date.strftime("%Y-%m-%d")
        # Move the current date forward by one day
        self.current_date += timedelta(days=1)
        return date_str
