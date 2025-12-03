def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

is_palindrome("MOM")
