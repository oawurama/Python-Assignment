name = input ('Enter name: ')
year = int(input('Enter the year you were born : '))
month = int(input('Enter the month you were born(1 to 12) : '))
day = int(input('Enter day of the month you were born(1-31): '))


if month == 1:
    month = month + 12
    year = year - 1
elif month == 2:
    month = month + 12
    year = year - 1

century = (year // 100)
century_year = (year % 100)


dotw = (day + ((26 * (month + 1)) // (10)) + century_year + ((century_year) // \
    (4)) + ((century) // (4)) + (5 * century)) % 7

if dotw == 0:
    print('Hi {}, Did you know that you were born on a Saturday?' . format (name))
elif dotw == 1:
    print('Hi {}, Did you know that you were born on a Sunday? ')
elif dotw == 2:
    print('Hi {}, Did you know that you were born on a Monday?' . format (name))
elif dotw == 3:
    print('Hi {}, Did you know that you were born on a Tuesday?' . format (name))
elif dotw == 4:
    print('Hi {},  Did you know that you were born on a Wednesday?' . format (name))
elif dotw == 5:
    print('Hi {}, Did you know that you were born on a Thursday ?' . format (name))
elif dotw == 6:
    print('Hi {}, Did you know that you were born on a Friday?' . format (name))



