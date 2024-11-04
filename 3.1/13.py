
#
def is_dunder(a):
    b = f'{a[:2:]}' + f'{a[:len(a) - 3:-1]}'
    c = '____'
    if b == c:
        a = a[2:len(a) - 2]
        return all((a.isalpha(), len(a) >= 2))
    return False
        # if all((a.isalpha(), len(a) >= 2)):

        #     print(True)
        # else:
        #     print(False)
    # else:
        # print(False)


print(is_dunder('__abvc3__'))
