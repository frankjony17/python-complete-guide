"""
    Find substrings that contain all vowels

    We have been given a string in lowercase alphabets. We need to print substrings that contain
    all the vowels at least one time and there are no consonants (non-vowel characters) present in
    the substrings.

    Examples:
        Input : str = aeoibddaeoiud
        Output : aeoiu

        Input : str = aeoibsddaeiouudb
        Output : aeiou, aeiouu
        Reference:- Samsung Interview Questions.

    Recommended:
        Please try your approach on {IDE} first, before moving on to the solution.
        We use a hashing based technique and start traversing the string from the start.
        For every character, we consider all substrings starting from it.
        If we encounter a consonant, we move to the next starting character.
        Else, we insert the current character in a hash.
        If all vowels are included, we print the current substring.
"""


# Returns true if x is vowel.
def is_vowel(v):
    if v in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False


# First solution:
def find_substring_1(str_1):
    # Outer loop picks starting character and inner loop picks ending character.
    n = len(str_1)
    for i in range(n):
        _hash = dict()

        for j in range(i, n):

            # If current character is not vowel,
            # then no more result substrings
            # possible starting from str1[i].
            if not is_vowel(str_1[j]):
                break

            # If vowel, then we insert it in hash
            _hash[str_1[j]] = 1

            # If all vowels are present in current substring
            if len(_hash) == 5:
                print(str_1[i:j + 1], end=" ")


# Driver code
str_1 = "aeoibsddaeiouudb"
find_substring_1(str_1)

"""
    Optimized Solution: For every character, If current character is vowel then insert into hash.
    Else set flag Start to next substring start from i+1th index. 
    If all vowels are included, we print the current substring. 
"""


# Function to FindSubstrings of string
def find_substring_2(str_2):
    _hash = set()
    start = 0

    for i in range(len(str_2)):
        # If current character is vowel
        # then insert into hash
        if is_vowel(str_2[i]):
            _hash.add(str_2[i])

            # If all vowels are present
            # in current substring
            if len(_hash) == 5:
                print(str_2[start: i + 1], end=" ")
        else:
            start = i + 1
            _hash.clear()


# Driver Code
_str_2 = "aeoibsddaeiouudb"
find_substring_2(_str_2)
