def product(lst, start=1):
    return sum([i * start for i in lst])


print(product([1, 2, 3], start=10))
