from lab_1_4exmp import get_my_string


def is_palindrome(s):

    s = s.replace(" ", "").lower()
    return s == s[::-1]


# Check if the imported string is a palindrome
if is_palindrome(get_my_string()):
    print(f'"{get_my_string()}" is a palindrome.')
else:
    print(f'"{get_my_string()}" is not a palindrome.')

