# White a function

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    if leap == True:
        print('Is leap year')
    else:
        print('Not leap year')
    return leap

is_leap(int(input('Input year: ')))