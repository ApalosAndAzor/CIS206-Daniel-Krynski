def get_year():
    year = int(input("Enter the year in A.D. : "))
    return year


def get_month():
    month = int(input("Enter the month in the form of [1-12]: "))
    return month


def calculate_leap(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False


def get_month_name(month):
    months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "Novermber",
        "December"]
    month_name = months[month - 1]
    return month_name    


def get_month_days(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if calculate_leap(year):
        days[1] = 29
    month_days = days[month - 1]
    return month_days


def display_results(month_name, month_days):
    print()
    print("Month name: " + month_name)
    print("Days: ", month_days)


def main():
    while True:
        year = get_year()
        if year <= 0:
            break

        month = get_month()
        if month < 1 or month > 12:
            break

        month_name = get_month_name(month)
        month_days = get_month_days(year, month)
        display_results(month_name, month_days)


main()