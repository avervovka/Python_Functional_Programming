def is_palindrome(string):
    string = string.replace(' ', '').upper()
    return string == string[::-1]


print(is_palindrome('Never Odd or Even'))

