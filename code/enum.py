# enum: Enumeration Type
# The enum module defines an enumeration type with iteration and comparison capabilities. It can be 
# used to create well-defined symbols for values, instead of using literal integers or strings.

import enum


# ----------------------------------
# enum: Enumeration Type
# A new enumeration is defined using the class syntax by subclassing Enum and adding class attributes 
# describing the values. The members of the Enum are converted to instances as the class is parsed. 
# Each instance has a name property corresponding to the member name and a value property corresponding 
# to the value assigned to the name in the class definition.

class Weekday(enum.Enum): 
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

print('\nMember name: {}'.format(Weekday.Monday.name)) 
print('Member value: {}'.format(Weekday.Monday.value))


# ----------------------------------
# Comparing Enums
# Because enumeration members are not ordered, they support only comparison by identity and equality. 
# Use the IntEnum class for enumerations where the members need to behave more like numbers—for 
# example, to support comparisons

class Weekday(enum.IntEnum): 
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

print('\n'.join(s.name for s in sorted(Weekday)))


# ----------------------------------
# Unique Enumeration Values
# Enum members with the same value are tracked as alias references to the same member object. 
# Aliases do not cause repeated values to be present in the iterator for the Enum.

class Weekday(enum.IntEnum): 
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

    Mon = 1
    Tues = 2
    Fri = 5

print("Monday is Mon:", Weekday.Monday is Weekday.Mon)

# To require all members to have unique values, add the @unique decorator to the Enum.

@enum.unique 
class Weekday(enum.IntEnum): 
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

    # This will trigger an ValueError: duplicate values found in <enum 'Weekday'>: Mon -> Monday, Tues -> Tuesday, Fri -> Friday
    # Mon = 1
    # Tues = 2
    # Fri = 5


# ----------------------------------
# Creating Enumerations Programmatically
# In some cases, it is more convenient to create enumerations programmatically, rather than 
# hard-coding them in a class definition. For those situations, Enum also supports passing 
# the member names and values to the class constructor.

Weekday = enum.Enum(
    value = 'Weekday',
    names = ("Monday Tuesday Wednesday Thursday Friday")
)

for day in Weekday: 
    print('{:15} = {}'.format(day.name, day.value))

# For more control over the values associated with members, the names string can be replaced 
# with a sequence of two-part tuples or a dictionary mapping names to values.


# ----------------------------------
# Non-integer Member Values
# Enum member values are not restricted to integers. In fact, any type of object can be 
# associated with a member. If the value is a tuple, the members are passed as individual 
# arguments to __init__().


class Weekday(enum.Enum): 
    Monday = (1, "Tuesday")
    Tuesday = (2, "Wednesday")
    Wednesday = (3, "Thursday")
    Thursday = (4, "Friday")
    Friday = (5, "Weekend!")

    def __init__(self, num, nextday):
        self.num = num
        self.nextday = nextday
    
    def stillwork(self):
        return self.nextday != "Weekend!"
    
print("Today is", Weekday.Monday.name)
print("Tomorrow is", Weekday.Monday.nextday)
print("Still have to work tomorrow?", Weekday.Monday.stillwork())

