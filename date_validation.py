from validation import *
from datetime import datetime, date

def is_month_day(value: []):
    day = value[0]
    month = value[1]
    year = value[2]
    if month in (4, 6, 9, 11) and day == 31:
        raise ValueError
    if month == 2:
        if day == 30:
            raise ValueError
        if not (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            if day == 29:
                raise ValueError
def is_valid(additional_condition=is_str, *value_for_conditional):
    try:
        return additional_condition(value_for_conditional)
    except ValueError as error:
        raise ValueError(error)

def is_date(value=None):
    if value == None:
        value = input()
    n = value
    n = n.split('.')
    filter(lambda x: x != '', n)
    if len(n) != 3:
        print('try again')
        return is_date()
    try:
        day = validate_numb(n[0])
        month = validate_numb(n[1])
        year = validate_numb(n[2])
        if day > 31 or month > 12 or year < 1950 or year > 2022:
            print('try again')
            return is_date()
        is_valid(is_month_day, day, month, year)
    except ValueError:
        print('try again')
        return is_date()
    return '.'.join([str(day), str(month), str(year)])

def updated_at(first, second= None) :
    f_day = first
    f_day = f_day.split('.')
    second = is_date(second)
    s_day = second
    s_day = s_day.split('.')
    date1 = date(int(f_day[2]), int(f_day[1]), int(f_day[0]))
    date2 = date(int(s_day[2]), int(s_day[1]), int(s_day[0]))
    if date1 >= date2:
        print('try again, update should be after created_at ')
        updated_at(first, second=None)
    return second
    # date1 = date(1995, 3, 20)
    #              18.7.2001



