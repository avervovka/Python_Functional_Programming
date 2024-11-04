def is_leap(year):
    return (all([year % 4 == 0,
            year % 100 != 0])
            or year % 400 == 0)


def count_leap_years(y1, y2):
    a = 0
    for i in range(y1, y2 + 1):
        if is_leap(i):
            a += i
            break
    if a != 0:
        gen = [i for i in range(a, y2, 4) if is_leap(i) is True]
        return gen
    else:
        return []


print(count_leap_years(2000, 2018))
