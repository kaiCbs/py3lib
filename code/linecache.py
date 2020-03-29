# linecache: Read Text Files Efficiently
# Thelinecachemodule is used within other parts of the Python standard library
# when dealing with Python source files.

import tempfile
import linecache
import os

# ------------------------------------------------------------------------------
#

text = """
The linecache module allows one to get any line from a Python source file, 
while attempting to optimize internally, using a cache, the common case where 
many lines are read from a single file. This is used by the traceback module 
to retrieve source lines for inclusion in the formatted traceback.

The tokenize.open() function is used to open files. This function uses 
tokenize.detect_encoding() to get the encoding of the file; in the absence of 
an encoding token, the file encoding defaults to UTF-8.
"""


def make_tempfile():
    fd, temp = tempfile.mkstemp()
    os.close(fd)
    with open(temp, "wt") as f:
        f.write(text)
    return temp


def cleanup(filename):
    os.unlink(filename)


filename = make_tempfile()

print(filename)
print("SOURCE:")
print("{!r}".format(text.split("\n")[4]))
print()
print("CACHE:")
print("{!r}".format(linecache.getline(filename, 5)))


# ------------------------------------------------------------------------------
# Error Handling
# If the requested line number falls out of the range of valid lines in the
# file, getline() returns a empty string

not_exist = linecache.getline(filename, 500)

print(
    "NOT EXISTS: {!r} includes {} characters".format(not_exist, len(not_exist))
)

# Reading from a file that does not exist is handled in the same way.

not_exist = linecache.getline("fake file", 500)

print(
    "NOT EXISTS: {!r} includes {} characters".format(not_exist, len(not_exist))
)

cleanup(filename)

# The module never raises an exception when the caller tries to read data


# ------------------------------------------------------------------------------
# Reading Python Source Files
# Since linecache is used so heavily when producing tracebacks, one of its key
# features is theability to find Python source modules in the import path by
# specifying the base name of the module

for i in range(5):
    print(linecache.getline("linecache.py", i + 1))

file_src = linecache.__file__
print(file_src)

with open(file_src, "r") as f:
    file_line = "".join(f.readlines()[:5])
print(file_line)
