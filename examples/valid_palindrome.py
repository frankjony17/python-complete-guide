"""
    Given a non-empty string value, you may delete at most one character.
    Judge whether you can make it a palindrome.

    The string will only contain lowercase characters a-z.
"""
value = 'radkar'


def palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]

        if t == t[::-1]:
            return True, s[i]

    return s == s[::-1]


print(palindrome(value))
