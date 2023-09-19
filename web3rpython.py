
"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def string(val):
    string_end = val[-3:]
    if len(val) > 3:
        if string_end != 'ing':
            val = val + 'ing'
            return val
        elif string_end == 'ing':
            val = val[:-3] + 'ly'
            return val
    else:
        return val

val = input("enter: ")
print(string(val))
