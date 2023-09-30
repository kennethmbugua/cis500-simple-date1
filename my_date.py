#######################################################
# my_date
#
# Name: Kenneth Mbugua
# Section: XX
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    if(year%4==0 and year%100!=0 or year%400==0):
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
    #Getting the days before year1 was over
   if(is_leap_year(year1)):
       days_elapsed_year1 = 366-ordinal_date(year1,month1,day1)
   else:
       days_elapsed_year1 = 365 - ordinal_date(year1, month1, day1)
#Getting days on current year from Jan to month2
   if is_leap_year(year2):
        days_elapsed_year2 = ordinal_date(year2, month2, day2)

   else:
       days_elapsed_year2 =  ordinal_date(year2, month2, day2)

#Getting the days in the years between if there were more than one year in between
   more_than_one = year2 - year1
   specific_y = year1 + 1
   total_days_in_y = 0
   total_days_in_yl = 0
   if (more_than_one > 1):
       for year_in in range(more_than_one - 1):
           specific_year = specific_y + year_in

           if (is_leap_year(specific_year)):
               total_days_in_yl = total_days_in_yl + 366
           else:
               total_days_in_y += 365
   total_days_in_y + total_days_in_yl #Getting total days
   total_days_elapsed = total_days_in_yl+total_days_in_y +days_elapsed_year1+days_elapsed_year2
   return total_days_elapsed


def day_of_week(year: int, month: int, day: int) -> str:
    DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    current_day = ("Sunday")
    dnum = DAYS_OF_WEEK.index(current_day)
    specific_day =(days_elapsed(year,month,day,2020,5,17)-dnum)% 7
    specific_day=7-specific_day
    if(specific_day==7):
        specific_day=0
    else:
        specific_day=specific_day

    i = DAYS_OF_WEEK[specific_day]
    return i



def to_str(year: int, month: int, day: int) -> str:

    month_name = ("0","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")

    return f"{day_of_week(year,month,day)}, {day}, {month_name[month]}, {year}"

print(to_str(1833,3,7))


