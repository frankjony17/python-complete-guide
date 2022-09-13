"""
  Create a list of all the consonants in the string
    “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
"""
string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

consonants = [letter for letter in string if letter not in ["a", "e", "i", "o", "u"]]

print(consonants)
