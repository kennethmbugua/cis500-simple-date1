#######################################################
# my_date
#
# Name: Kenneth Mbugua
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
        return True
    else:
        return False
    # """Return True if year is a leap year, False otherwise"


def ordinal_date(year: int, month: int, day: int) -> int:
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28

    sum_of_days = 0

    for i, days in enumerate(day_in_month):
        if i < month:
            sum_of_days = sum_of_days + days
        elif (i == 1):
            sum_of_days = 0
    return sum_of_days + day


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    day_in_month2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year2):
        day_in_month2[2] = 29
    else:
        day_in_month2[2] = 28
    sum_of_days2 = 0
    for i, days2 in enumerate(day_in_month2):
        if i < month2:
            sum_of_days2 = sum_of_days2+days2
    sum_of_days2=sum_of_days2+day2
    if is_leap_year(year1):
        year1_days = 366 - ordinal_date(year1, month1, day1)
    else:
        year1_days = 365 - ordinal_date(year1, month1, day1)
    return sum_of_days2+year1_days





def day_of_week(year: int, month: int, day: int) -> str:
    DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    current_day = ("Wednesday")
    dnum = DAYS_OF_WEEK.index(current_day)



    specific_day =(days_elapsed(year,month,day,2020,5,13)-dnum)% 7
    specific_day=7-specific_day
    if(specific_day==7):
        specific_day=0
    else:
        specific_day=specific_day

    i = DAYS_OF_WEEK[specific_day]
    return i

    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    # pass


def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    month_name = ("0","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")

    return f"{day_of_week(year,month,day)}, {day}, {month_name[month]}, {year}"




