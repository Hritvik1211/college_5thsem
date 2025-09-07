from datetime import datetime, timedelta

def count_sundays_between_dates(start_date_str, end_date_str):

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    

    if start_date > end_date:
        start_date, end_date = end_date, start_date


    sunday_count = 0


    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6:
            sunday_count += 1
        current_date += timedelta(days=1)

    return sunday_count



start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")


sundays = count_sundays_between_dates(start_date, end_date)
print(f"Number of Sundays between {start_date} and {end_date}: {sundays}")
