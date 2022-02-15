import re
def is_palindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    return strs == strs[::-1]


def is_palindrome_faster(s: str) -> bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s) # regular expression
    return s==s[::-1]


s = input()
if is_palindrome_faster(s):
    print("true")
else:
    print("false")
