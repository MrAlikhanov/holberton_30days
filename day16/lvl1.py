# Day 16 - Date Time

from datetime import datetime, timedelta

# 1. Current day, month, year, hour, minute and timestamp
now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# 2. Format current date
formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted:", formatted)  # 04/18/2026, 14:35:20

# 3. Convert string to datetime
date_string = '5 December, 2019'
parsed_date = datetime.strptime(date_string, '%d %B, %Y')
print("Parsed date:", parsed_date)  # 2019-12-05 00:00:00

# 4. Time difference between now and new year
new_year = datetime(now.year + 1, 1, 1)
time_to_new_year = new_year - now
print(f"Time until New Year: {time_to_new_year.days} days, "
      f"{time_to_new_year.seconds // 3600} hours, "
      f"{(time_to_new_year.seconds % 3600) // 60} minutes")

# 5. Time difference between 1 Jan 1970 and now
epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch
print(f"Days since 1 Jan 1970: {time_since_epoch.days} days")
print(f"Seconds since 1 Jan 1970: {int(time_since_epoch.total_seconds())}")

# 6. Practical uses of datetime module

# Time series analysis - tracking data points over time
events = [
    {'event': 'Server started',  'time': datetime(2026, 4, 18, 8,  0,  0)},
    {'event': 'User logged in',  'time': datetime(2026, 4, 18, 9,  15, 0)},
    {'event': 'Error occurred',  'time': datetime(2026, 4, 18, 10, 30, 0)},
]
for e in events:
    print(f"{e['event']} at {e['time'].strftime('%H:%M:%S')}")

# Timestamp for app activities
def log_activity(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {activity}")

log_activity("User signed up")
log_activity("File uploaded")

# Blog post scheduling
def is_post_published(publish_date):
    return datetime.now() >= publish_date

post_date = datetime(2026, 4, 1)
print("Post is published:", is_post_published(post_date))  # True

future_post = datetime(2027, 1, 1)
print("Future post is published:", is_post_published(future_post))  # False
