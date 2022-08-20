# https://www.pythontutorial.net/python-oop/python-dataclass/
from dataclasses import dataclass, astuple, asdict, field

# 1 --------------------------------------------------------------------------------------------------------------------
"""
 In this example, the Person class has two attributes name
 with the type str and age with the type int. By doing this,
 the @dataclass decorator implicitly creates the __init__ method like this:
"""


@dataclass
class Person1:
    name: str
    age: int


p = Person1('John', 25)  # Person(name='John', age=25)

"""
 Also, if you compare two Person‘s objects with the same attribute value,
 it’ll return True. For example:
"""
p1 = Person1('John', 25)
p2 = Person1('John', 25)

print(p1 == p2)  # True

# 2 --------------------------------------------------------------------------------------------------------------------

# Default values:


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100


print(Person('John Doe', 25))  # Person(name='John Doe', age=25, iq=100)

# 3 --------------------------------------------------------------------------------------------------------------------
"""
  Convert to a tuple or a dictionary
  The dataclasses module has the astuple() and asdict() functions 
  that convert an instance of the dataclass to a tuple and a dictionary. For example:
"""


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100


p3 = Person('John Doe', 25)

print(astuple(p3))  # ('John Doe', 25, 100)
print(asdict(p3))  # {'name': 'John Doe', 'age': 25, 'iq': 100}

# 4 --------------------------------------------------------------------------------------------------------------------
"""
  Create immutable objects:
  To create readonly objects from a dataclass, 
  you can set the frozen argument of the dataclass decorator to True. For example:
"""


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    iq: int = 100


p4 = Person('Jane Doe', 25)
p4.iq = 120  # dataclasses.FrozenInstanceError: cannot assign to field 'iq'

# 5 --------------------------------------------------------------------------------------------------------------------
"""
  Customize attribute behaviors.
  If don’t want to initialize an attribute in the __init__ method, 
  you can use the field() function from the dataclasses module.

  The following example defines the can_vote attribute that is initialized using the __init__ method:
"""


class Person:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)


"""
  If you want to initialize an attribute that depends on the value of another attribute,
  you can use the __post_init__ method. As its name implies, 
  Python calls the __post_init__ method after the __init__ method.

  The following use the __post_init__ method to initialize the can_vote attribute
  based on the age attribute:
"""


@dataclass
class Person:
    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        print('called __post_init__ method')
        self.can_vote = 18 <= self.age <= 70


p5 = Person('Jane Doe', 25)
print(p5)
# called the __post_init__ method
# Person(name='Jane Doe', age=25, iq=100, can_vote=True)

# 6 --------------------------------------------------------------------------------------------------------------------
"""
  Sort objects
  By default, a dataclass implements the __eq__ method.

  To allow different types of comparisons like __lt__, __lte__, __gt__, __gte__,
   you can set the order argument of the @dataclass decorator to True:
"""
"""
  To do that, you need to:

  First, pass the order=True parameter to the @dataclass decorator.
  Second, define the sort_index attribute and set its init parameter to False.
  Third, set the sort_index to the age attribute in the __post_init__ method
   to sort the Person‘s object by age.
   
  The following shows the code for sorting Person‘s objects by age:
"""


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        # sort by age
        self.sort_index = self.age


members = [
    Person(name='John', age=25),
    Person(name='Bob', age=35),
    Person(name='Alice', age=30)
]

sorted_members = sorted(members)
for member in sorted_members:
    print(f'{member.name}(age={member.age})')

# John(age=25)
# Alice(age=30)
# Bob(age=35)

# ----------------------------------------------------------------------------------------------------------------------
"""
Summary:
    Use the @dataclass decorator from the dataclasses module to make a class a dataclass.
     The dataclass object implements the __eq__ and __str__ by default.
    
    Use the astuple() and asdict() functions to convert an object of a dataclass to a tuple
     and dictionary.
    
    Use frozen=True to define a class whose objects are immutable.
    
    Use __post_init__ method to initalize attributes that depends on other attributes.
    
    Use sort_index to specify the sort attributes of the dataclass objects.
"""
