def powers(num):
    square = num**2
    cube = num**3
    return [num, square, cube]


values = powers(4)
print(values)
print(type(values))
