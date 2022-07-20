# def palindrome(s):
#     new_string = ''
#     for char in s:
#         if char.isalpha():
#             new_string += char

#     if new_string.lower() == "".join(reversed(new_string.lower())):
#         return True

#     return False
from re import sub

def palindrome(s):

    new_string = sub(r'[\W_]*', '', s).lower()
    # sub function searches for the PATTERN in the string an replaces the 
    # matched with the replacement
    # PATTERN: r'[\W_]+'
        # \W not a word character and _ (underscore)
    # REPLACEMENT: ''
    # s - our string

    # I believe that RegEx is super FAST :D

    # O(n) - Linear time
    temp_string = ''
    for char in new_string:
        temp_string = char + temp_string

    if new_string == temp_string:
        return True
    
    return False
