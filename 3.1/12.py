def is_strings_equal(string, second_string):
    if sorted(string) == sorted(second_string):
        return True
    return False


print(is_strings_equal("aabcb", "bcaba"))
