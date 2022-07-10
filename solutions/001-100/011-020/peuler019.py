# Project Euler - 19
# Date: 31/05/2022

days = ['sun','mon','tue','wed','thu','fri','sat']
months = [31,28,31,30,31,30,31,31,30,31,30,31]
months_leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
def is_leap_year(year):
    if year%100 == 0 and year%400 != 0:
        return False
    elif year%100 == 0 and year%400 == 0:
        return True
    elif year%4==0:
        return True
    else:
        return False
def create_calendar_year(year,first_weekday):
    weekday_list = []
    weekday_by_month =[[],[],[],[],[],[],[],[],[],[],[],[]]
    start_index = days.index(first_weekday)
    counter = 0
    if is_leap_year(year):
        for i in range(366):
            weekday_list.append(days[(start_index+i)%7])
        for i in range(len(months_leap_year)):
            for j in range(months_leap_year[i]):
                weekday_by_month[i].append(weekday_list[counter + j])
            counter += months[i]
        return weekday_by_month
    else:
        for i in range(365):
            weekday_list.append(days[(start_index+i)%7])
        for i in range(len(months)):
            for j in range(months[i]):
                weekday_by_month[i].append(weekday_list[counter + j])
            counter += months[i]
        return weekday_by_month
def find_num_sun(calendar_year):
    counter = 0
    for i in range(len(calendar_year)):
        if calendar_year[i][0] == 'sun':
            counter += 1
    return counter

last_weekday = 'mon'
tally = 0
first_weekday = days[(days.index(last_weekday)+1)%7]
for year in range(1901,2001):
    first_weekday = days[(days.index(last_weekday)+1)%7]
    calendar_year = create_calendar_year(year, first_weekday)
    tally += find_num_sun(calendar_year)
    last_weekday = calendar_year[-1][-1]
print(tally)