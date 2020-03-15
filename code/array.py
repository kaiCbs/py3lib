# array: Sequence of Fixed-Type Data
# The array module defines a sequence data structure that looks very much like a list, except that all
# of the members have to be of the same primitive type. The types supported are all numeric or other
# fixed-size primitive types such as bytes.

import array
import binascii
import tempfile


# ----------------------------------
# Initialization
# An array is instantiated with an argument describing the type of data to be allowed, and possibly
# an initial sequence of data to store in the array.
# Type Codes for array Members
# Code      Type                Minimum Size (Bytes)
# b         Int                 1
# B         Int                 1
# h         Signed short        2
# H         Unsigned short      2
# i         Signed int          2
# I         Unsigned int        2
# l         Signed long         4
# L         Unsigned long       4
# q         Signed long long    8
# Q         Unsigned long long  4
# f         Float               4
# d         Double float        8

s = b"This is the array."
a = array.array("b", s)

print("As byte string:", s)
print("As array:", a)
print("As hex:", binascii.hexlify(a))


# ----------------------------------
# Manipulating Arrays
# An array can be extended and otherwise manipulated in the same ways as other Python sequences.

a = array.array("i", range(5))
print(a)
a.extend(range(5))
print(a)
print(a[1:-1])


# ----------------------------------
# Arrays and Files
# The contents of an array can be written to and read from files using built-in methods coded
# efficiently for that purpose.

output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

with open(output.name, "rb") as input:
    raw = input.read()
    print("Raw contents:", binascii.hexlify(raw))

    a2 = array.array("i")
    a2.fromfile(input, len(a))
    print("A2:", a2)


# ----------------------------------
# Alternative Byte Ordering
# If the data in the array is not in the native byte order, or if the data needs to be swapped
# before being sent to a system with a different byte order (or over the network), it is
# possible to convert the entire array without iterating over the elements from Python.

# The byteswap() method switches the byte order of the items in the array from within C, so
# it is much more efficient than looping over the data in Python.

# TODO: add example here
