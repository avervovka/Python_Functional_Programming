def create_palindrome(string):
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return string
    return f'{string}_i_{reversed_string}'


print(create_palindrome('mjvhjdgfb'))
