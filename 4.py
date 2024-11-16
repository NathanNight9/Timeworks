import time
from datetime import datetime

print(f"Current date and time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")
print(f"Current year: {datetime.now().year}")
print(f"Current month: {datetime.now().strftime("%B")}")
print(f"Week number: {datetime.now().strftime("%W")}")
print(f"Day number of the week: {datetime.now().weekday()}")
print(f"Day number of the year: {datetime.now().timetuple().tm_yday}")
print(f"Day number of the month: {datetime.now().timetuple().tm_mday}")
print(f"Current day: {datetime.now().strftime("%A")}")
