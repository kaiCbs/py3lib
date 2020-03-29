# fnmatch: Unix-Style Glob Pattern Matching
# The fnmatch module is used to compare filenames against glob -style patterns
# such as those used by Unix shells.

import fnmatch
import os

# ------------------------------------------------------------------------------
# Simple Matching
# fnmatch() compares a single filename against a pattern and returns a boolean
# value, indicating whether they match

pattern = "?????.py"

files = os.listdir("code")
for name in files:
    print("Filename: {:<25} {}".format(name, fnmatch.fnmatch(name, pattern)))


# To force a case-sensitive comparison, regardless of the file system and
# operating system settings, use fnmatchcase()


# ------------------------------------------------------------------------------
# Filtering
# To test a sequence of filenames, use filter() , which returns a list of the
# names that match the pattern argument

print(fnmatch.filter(files, pattern))


# ------------------------------------------------------------------------------
# Translating Patterns
# internally, fnmatch converts the glob pattern to a regular expression and
# uses the re module to compare the name and pattern.

print("Pattern :", pattern)
print("Regex   :", fnmatch.translate(pattern))
