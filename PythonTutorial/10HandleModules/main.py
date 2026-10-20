from temp import *

# Using functions from temp1.py
print(add(10, 20, 30));
print(sub(10, 20, 30));
print(mul(10, 20, 30));
print(div(10, 20));

# Using functions from temp2.py
greet("Alice")
greet_morning("Bob")
greet_evening("Charlie")

# Using functions from temp3.py
print("Current Date and Time:", get_current_datetime())
print("Current Date:", get_current_date())
print("Current Time:", get_current_time())
now = get_current_datetime()
print("Formatted Date and Time:", format_datetime(now, "%d-%m-%Y %I:%M %p"))

# Note = 1. This the proffesional way to handle modules in python.
# 2. If you don't want to use this approach then you can simple import using this way:
# from temp.temp1 import add, sub, mul, div
# from temp.temp2 import greet, greet_morning, greet_evening    
# from temp.temp3 import get_current_datetime, get_current_date, get_current_time, format_datetime
# 3. You can also import all the functions using this way:
# from temp.temp1 import *
# 4. But even thought you use this way, but always prefer to use __init__.py file to handle modules.