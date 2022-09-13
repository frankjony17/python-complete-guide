"""
  Count the number of spaces in a string
"""
some_string = 'the slow solid squid swam sumptuously through the slimy swamp'

spaces = [s for s in some_string if s == ' ']
print(len(spaces))
