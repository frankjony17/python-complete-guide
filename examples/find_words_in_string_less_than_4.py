"""
  Find all of the words in a string that are less than 4 letters
"""
string = 'On a summer day somner smith went simming in the sun and his red skin stung'

words = [word for word in string.split() if len(word) < 4]

print(words)
