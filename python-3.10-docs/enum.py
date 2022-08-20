# https://www.pythontutorial.net/python-oop/python-enum-unique/

# 1 --------------------------------------------------------------------------------------------------------------------
"""
    Introduction to the enum aliases
    By definition, the enumeration member values are unique. However, you can create different member names with the same values.

    For example, the following defines the Color enumeration:
"""
from enum import Enum


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3


"""
    In this example, the Color enumeration has the RED, CRIMSON, and SALMON members with the same value 1.

    When you define multiple members in an enumeration with the same values, 
    Python does not create different members but aliases.

    In this example, the RED is the main member while the CRIMSON and SALMON members are the aliases of the RED member

    The following statements return True because CRIMSON and SALMON members are RED meber:
"""
print(Color.RED is Color.CRIMSON)  # True
print(Color.RED is Color.SALMON)  # True
print(Color(1))  # Color.RED

"""
When you iterate the members of an enumeration with aliases, you’ll get only the main members,
 not the aliases.
For example:
"""
for color in Color:
    print(color)

# Color.RED
# Color.GREEN
# Color.BLUE

"""
To get all the members including aliases, you need to use the __member__ property of the enumeration class. 
For example:
"""
from pprint import pprint

pprint(Color.__members__)

# mappingproxy({'BLUE': <Color.BLUE: 3>,
#               'CRIMSON': <Color.RED: 1>,
#               'GREEN': <Color.GREEN: 2>,
#               'RED': <Color.RED: 1>,
#               'SALMON': <Color.RED: 1>})

# 2 --------------------------------------------------------------------------------------------------------------------
"""
    @enum.unique decorator
    To define an enumeration with no aliases, you can carefully use unique values for the members.
    For example:
"""
import enum


@enum.unique
class Day(enum.Enum):
    MON = 'Monday'
    TUE = 'Monday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

# ValueError: duplicate values found in <enum 'Day'>: TUE -> MON
