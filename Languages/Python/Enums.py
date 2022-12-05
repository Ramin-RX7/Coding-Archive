"""
Enum vs Class
    Can't be instantiated
    Can't be subclassed unless the base enum has no members
    Provide a human-readable string representation for their members
    Are iterable, returning their members in a sequence
    Provide hashable members that can be used as dictionary keys
    Support the square bracket syntax, call syntax, and dot notation to access members
    Don't allow member reassignments
"""


from enum import Enum, auto


#] Creating Enums
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = 3
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = 7

#] 
"""
>>> list(Day)
[<Day.MONDAY: 1>, <Day.TUESDAY: 2>, <Day.WEDNESDAY: 3>, <Day.THURSDAY: 4>,
 <Day.FRIDAY: 5>, <Day.SATURDAY: 6>, <Day.SUNDAY: 7>]
"""
print(list(Day))

#] 
"""
>>> type(Day.MONDAY)
<enum 'Day'>
"""


#] using methods
import string
class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]

class Alphabet(BaseTextEnum):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
"""
>>> Alphabet.LOWERCASE.as_list()
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""


#] Function API
# Enum(value,names,*,module=None,qualname=None,type=None,start=1)
HTTPMethod = Enum(
    "HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"]
)
"""
>>> list(HTTPMethod)
[ <HTTPMethod.GET: 1>,
  <HTTPMethod.POST: 2>,
  <HTTPMethod.PUSH: 3>,
  <HTTPMethod.PATCH: 4>,
  <HTTPMethod.DELETE: 5> ]
"""
HTTPStatusCode = Enum(
    value="HTTPStatusCode",
    names=[
        ("OK", 200),
        ("CREATED", 201),
        ("BAD_REQUEST", 400),
        ("NOT_FOUND", 404),
        ("SERVER_ERROR", 500),
    ],
)
"""
>>> list(HTTPStatusCode)
[ <HTTPStatusCode.OK: 200>,
  <HTTPStatusCode.CREATED: 201>,
  <HTTPStatusCode.BAD_REQUEST: 400>,
  <HTTPStatusCode.NOT_FOUND: 404>,
  <HTTPStatusCode.SERVER_ERROR: 500> ]
"""


#] Re-implementing auto() behaviour
class CardinalDirection(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name[0]
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
"""
>>> list(CardinalDirection)
[ <CardinalDirection.NORTH: 'N'>,
  <CardinalDirection.SOUTH: 'S'>,
  <CardinalDirection.EAST:  'E'>,
  <CardinalDirection.WEST:  'W'> ]
"""


#] If several members have same values, only the first one is shown
class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"
"""
>>> # Do not shows aliases
>>> list(OperatingSystem)
>>> # To access aliases, use __members__
>>> list(OperatingSystem.__members__.items())
"""
# Use "Unique" decorator to raise error when having similar values


#] Accessing Members
class CardinalDirection(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
"""
>>> # Dot notation
>>> CardinalDirection.NORTH
<CardinalDirection.NORTH: 'N'>
>>> # Call notation
>>> CardinalDirection("N")
<CardinalDirection.NORTH: 'N'>
>>> # Subscript notation
>>> CardinalDirection["NORTH"]
<CardinalDirection.NORTH: 'N'>
"""


#] .name and .value attributes
class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
"""
>>> Semaphore.RED.name
'RED'
>>> Semaphore.RED.value
1
>>> Semaphore.YELLOW.name
'YELLOW'
"""

