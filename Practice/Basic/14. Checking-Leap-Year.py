# A leap year is a year that is either:

# 1. Divisible by 4, and not divisible by 100, or
# 2.Divisible by 400.

year = int(input('Enter the Year: '))

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is NOT a leap year')