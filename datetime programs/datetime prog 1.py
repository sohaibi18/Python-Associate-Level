from datetime import datetime

# Create a datetime object for November 4, 2020, 14:53:00
dt = datetime(2020, 11, 4, 14, 53, 0)

# Display each result using the strftime method with appropriate directives
print(dt.strftime('%Y/%m/%d %H:%M:%S'))  # 2020/11/04 14:53:00
print(dt.strftime('%y/%B/%d %I:%M:%S %p'))  # 20/November/04 02:53:00 PM
print(dt.strftime('%a, %Y %b %d'))  # Wed, 2020 Nov 04
print(dt.strftime('%A, %Y %B %d'))  # Wednesday, 2020 November 04
print(f"Weekday: {dt.strftime('%w')}")  # Weekday: 3 (0 is Sunday, 3 is Wednesday)
print(f"Day of the year: {dt.strftime('%j')}")  # Day of the year: 309
print(f"Week number of the year: {dt.strftime('%U')}")  # Week number of the year: 44 (week starts on Sunday)

