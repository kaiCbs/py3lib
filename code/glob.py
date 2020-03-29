# glob: Filename Pattern Matching
# The pattern rules for glob are not the same as the rules for the regular
# expressions used by the re (page 13) module. Instead, they follow standard
# Unix path expansion rules.


import glob
import os
import pathlib


# ------------------------------------------------------------------------------
# Wildcards
# An asterisk (*) matches zero or more characters in a segment of a name

cwd = os.getcwd()
for name in sorted(glob.glob(cwd + "/code/*.py")):
    print(name)


# ------------------------------------------------------------------------------
# Single-Character Wildcard
# A question mark is another wildcard charactor, it matches any single
# character in that position in the name.

print("????.py")
cwd = os.getcwd()
for name in sorted(glob.glob(cwd + "/code/????.py")):
    print(name)


# ------------------------------------------------------------------------------
# Character Ranges
# Use a character range ( [a-z] ) instead of a question mark to match one of
# several characters.

print("\nlibrary starts with r,s,t")
for name in sorted(glob.glob(cwd + "/code/[r-t]*.py")):
    print(name)


# ------------------------------------------------------------------------------
# Escaping Meta-characters
# The escape() function builds a suitable pattern in
# which the special characters are “escaped” so they are not expanded or
# interpreted as special by glob.

for char in "*?1":
    pathlib.Path("test%s.py" % char).touch()

print("Escaping Meta-characters:")
print(glob.glob("test{}.py".format(glob.escape("*"))))
print(glob.glob("test{}.py".format(glob.escape("?"))))
print("No escaping")
print(glob.glob("test{}.py".format("*")))

for char in "*?1":
    pathlib.Path("test%s.py" % char).unlink()
