import calendar

try:
    # Get values from the user
    year = int(input("Enter year (e.g., 2026): "))
    month = int(input("Enter month (1-12): "))

    # Check if month is valid
    if 1 <= month <= 12:
        print("\n" + calendar.month(year, month))
    else:
        print("Error: Month must be between 1 and 12.")

except ValueError:
    print("Error: Please enter numbers only.")
