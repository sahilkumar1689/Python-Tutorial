from datetime import datetime, date, time

def get_current_datetime():
    """Return the current date and time as a datetime object."""
    return datetime.now()

def get_current_date():
    """Return the current date."""
    return date.today()

def get_current_time():
    """Return the current time."""
    return datetime.now().time()

def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    """Format a datetime object as a string."""
    return dt.strftime(fmt)
