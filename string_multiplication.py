def string_multiply(str1, str2):
    # multiply two strings (non-negative ints) - DON'T convert to ints
    return str(valuate(str1) * valuate(str2))


def valuate(string):
    conversion = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    value = 0
    for i,v in enumerate(string):
        place = len(string) - i - 1
        multiplier = 10**(place)
        value += conversion[v] * multiplier
    return value