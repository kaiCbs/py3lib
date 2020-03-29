# tempfile: Temporary File System Objects
# Creating temporary files with unique names securely, so they cannot be
# guessed by some-one wanting to break the application or steal the data, is
# challenging. The temfile module provides several functions for creating
# temporary file system resources securely.

import tempfile
import os

# ------------------------------------------------------------------------------
# Temporary Files
# When we need temporary files to store data without the need to share the file
# with other programs, we should use TemporaryFile() function.
# This functioncreates a file, and on platforms where it is possible, unlinks
# the new file immediately.

print("Create a file from PID:")
filename = "/tmp/{}.txt".format(os.getpid())

with open(filename, "w+b") as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

os.remove(filename)

print("\nTemporaryFile:")
with tempfile.TemporaryFile() as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

# To open the file in text mode, set mode to 'w+t' when the file is created.

with tempfile.TemporaryFile(mode="w+t") as f:
    f.writelines(["first line\n", "second line\n"])
    f.seek(0)
    for line in f:
        print(line.strip())


# ------------------------------------------------------------------------------
# Named Files
# The NamedTemporaryFile() function creates a file without unlinking it, so it
# retains its name (accessed with the name attribute).

print("\nNamedTemporaryFile:")
with tempfile.NamedTemporaryFile() as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

# The file is removed after the handle is closed


# ------------------------------------------------------------------------------
# Spooled Files
# For temporary files containing relatively small amounts of data, it is likely
# to be more efficient to use a SpooledTemporaryFile because it holds the file
# contents in memory using an io.BytesIO or io.StringIO buffer until the data
# reaches a threshold size.

with tempfile.SpooledTemporaryFile(
    max_size=100, mode="w+t", encoding="utf-8"
) as temp:
    print("temp: {!r}".format(temp))

    for i in range(7):
        temp.write("A very long sentences")
        print(temp._rolled, temp._file)

# This example uses private attributes of the SpooledTemporaryFile to determine
# when the rollover to disk has happened. It is rarely necessary to check this
# status except when tuning the buffer size
# To explicitly cause the buffer to be written to disk, call the rollover() or
# fileno() method


# ------------------------------------------------------------------------------
# Predicting Name
# Names are generated using the following formula:
# ===   dir + prefix + random + suffix  ===

with tempfile.NamedTemporaryFile(
    suffix=".py", prefix="py3lib", dir="/tmp"
) as temp:
    print("temp: {!r}".format(temp))
    print("temp name: {!r}".format(temp.name))


# ------------------------------------------------------------------------------
# Temporary File Location
# If an explicit destination is not given using the dir argument, the path used
# for the temporary files will vary based on the current platform and settings

print("gettempdir():", tempfile.gettempdir())
print("gettempprefix():", tempfile.gettempprefix())

with tempfile.NamedTemporaryFile(suffix=".py", prefix="py3lib") as temp:
    print("temp: {!r}".format(temp))
    print("temp name: {!r}".format(temp.name))
