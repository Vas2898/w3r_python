rows = int(input("Enter value"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i, end = '')
    print()

rows = int(input("Enter value"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(rows, end = '')
    print()


def count(val):
    count = 0
    for i in val:   
        count = count + 1
    print(count)
val = input("enter: ")
count(val)


"""
Write a Python program to count the number of characters (character frequency) in a string.
google.com
"""


string = input("enter: ")
dic = {}
for i in string:
    keys = dic.keys()
    if i in keys:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)



"""
3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

"""


def string(val):
    if len(val) < 2:
        return "Empty"
    else:
        return val[:2] + val[-2:]
        
val = input("enter: ")
print(string(val))


"""
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""


def string(val):
    char = val[0]
    val = val.replace(char,'$')
    val = char + val[1:]
    return val

val = input("enter: ")
print(string(val))

