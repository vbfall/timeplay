

# Receives a date in string format and returns its separate parts
def parse_date(date_string):
    month_names = {1: 'January',
                    2: 'February',
                    3: 'March',
                    4: 'April',
                    5: 'May',
                    6: 'June',
                    7: 'July',
                    8: 'August',
                    9: 'September',
                    10: 'October',
                    11: 'November',
                    12: 'December'
                    }

    date_day = int(date_string[8:])

    date_month = int(date_string[:7][5:])
    date_month_name = month_names[date_month]

    date_year = int(date_string[:4])

    return date_year, date_month, date_month_name, date_day
# end of parse_date()


# acquire name
print('\n\nPlease tell me your name: ', end='')
name = input()
print('Hello', name, '\n')

# acquire current date
print('Please tell me what day it is today (yyyy-mm-dd): ', end='')
current_date = input()
current_year, current_month, current_month_name, current_day = parse_date(current_date)

print('So, today is the', current_day,
        'th of', current_month_name,
        'in the year', current_year,
        '... \n')

# acquire birth date
print('Please tell me your birthday (yyyy-mm-dd): ', end='')
birth_date = input()
birth_year, birth_month, birth_month_name, birth_day = parse_date(birth_date)

print('... and you were born on', birth_day,
        'th of', birth_month_name,
        'in the year', birth_year,
        '...\n')

days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# count days in birth year
num_days = (days_per_month[birth_month] - birth_day)
count_month = birth_month + 1
while(count_month <= 12):
    num_days = num_days + days_per_month[count_month]
    count_month = count_month + 1

count_year = birth_year + 1
# count days in full years
while(count_year < current_year):
    num_days = num_days + 365
    if(count_year%4 == 0):
        num_days = num_days + 1
    count_year = count_year + 1

# count days in current year
count_month = 1
while(count_month < current_month):
    num_days = num_days + days_per_month[count_month]
    count_month = count_month + 1
num_days = num_days + (current_day - 1) # not counting today

num_hours = 24 * num_days

print(name, ', you have lived for', num_days, 'days!')
print(name, ', you have lived for', num_hours, 'hours!')

print('\n\n\n\n')
