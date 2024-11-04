def is_leap(year):
    return (all([year % 4 == 0,
            year % 100 != 0])
            or year % 400 == 0)


print(is_leap(int(input())))
