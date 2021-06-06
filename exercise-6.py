# exercise-06 What's the  Season?


input_month = input("Enter the month of the year (Jan - Dec):")
month= input_month.lower()
day = int(input("Enter the day of the month:"))

if month in ('jan','feb'):
    print(f'{input_month} {day} is in Winter')
if (month == 'dec' and day > 20) or (month == 'mar' and day < 20):
    print(f'{input_month} {day} is in Winter')

if month in ('apr','may'):
    print(f'{input_month} {day} is in Spring')
if (month == 'mar' and day > 19) or (month == 'jun' and day < 21):
    print(f'{input_month} {day} is in Spring')

if month in ('jul','aug'):
    print(f'{input_month} {day} is in Summer')
if (month == 'jun' and day > 20) or (month == 'sep' and day < 22):
    print(f'{input_month} {day} is in Summer')

if month in ('oct','nov'):
    print(f'{input_month} {day} is in Fall')
if (month == 'sep' and day > 21) or (month == 'dec' and day < 21):
    print(f'{input_month} {day} is in Fall')




