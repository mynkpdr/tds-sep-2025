import datetime

start_date_str = "1980-02-07"
end_date_str = "2014-01-26"

start_date = datetime.date.fromisoformat(start_date_str)
end_date = datetime.date.fromisoformat(end_date_str)

weekend_count = 0
current_date = start_date

while current_date <= end_date:
    # weekday() returns 5 for Saturday and 6 for Sunday
    if current_date.weekday() >= 5:
        weekend_count += 1
    current_date += datetime.timedelta(days=1)

print(f"Total weekend days: {weekend_count}")
