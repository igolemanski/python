def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



def days_in_month(year_chosen, month_chosen):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_chosen) == True and month_chosen == 2:
        month_days[1] = 29
        return month_days[1]
    else:
        return month_days[month_chosen - 1]

# Do not change
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)