# os.path: Platform-Independent Manipulation of Filenames
# Writing code to work with files on multiple platforms is easy using the
# functions included in the os.path module. Even programs not intended to be
# ported between platforms should use os.path for reliable filename parsing.

import os.path
import os
import time


# ------------------------------------------------------------------------------
# Parsing Path
# Path parsing depends on a few variables defined in os

print(
    "curdir: {}".format(os.path.curdir),
    "pardir: {}".format(os.path.pardir),
    "sep: {}".format(os.path.sep),
    "extsep: {}".format(os.path.extsep),
    sep="\n",
)

# split() breaks the path into two separate parts and returns a tuple. When the
# input argument ends in os.sep, the last element of the path wil be empty.

paths = [
    "user/kai/files/temp.txt",
    "user/kai/files/",
    "user/kai/files",
    "user/kaifiles",
]

for path in paths:
    print("{!r:>25} : {}".format(path, os.path.split(path)))

# basename() returns a value equivalent to the second part of the split() value
# dirname() returns the first part of the split path

for path in paths:
    basename = os.path.basename(path)
    dirname = os.path.dirname(path)
    print("{!r:>25} : {}".format(path, (dirname, basename)))

# splitext() works like split(), but divides the path on the ext separator,
# rather than the directory separator.

for path in paths:
    print("{!r:>25} : {}".format(path, os.path.splitext(path)))

# commonprefix() takes a list of paths as an argument and returns a single
# string that represents a common prefix present in all of the paths
# commonpath() does honor path separators. It returns a prefix that does not
# include partial path values.

print("PREFIX:", os.path.commonprefix(paths))
print("PREFIX:", os.path.commonpath(paths))


# ------------------------------------------------------------------------------
# Building Paths
# To combine several path components into a single value, use join().
# Note that if any argument to join begins with os.sep , all of the previous
# arguments are discarded and the new one becomes the beginning of the result

base = "/home/kai/projects/dataset"

files = ["population.csv", "gpd.csv", "area.csv", "/share/user.csv"]

for file in files:
    print("{!r:>17} : {!r}".format(file, os.path.join(base, file)))


# Sometimes we can use some "“variable" components to construct paths.
# expanduser() converts the tilde(~) to the name of a user’s home directory

for user in ["", "kai", "unknown"]:
    lookup = "~" + user
    print("{!r:>17} : {!r}".format(lookup, os.path.expanduser(lookup)))

# expandvars() expands any shell environment variables present in the path

os.environ["NEWVAR"] = "newfolder"
print(os.path.expandvars("/home/user/$NEWVAR"))


# ------------------------------------------------------------------------------
# Normalizing Paths
# Use normpath() to clean verbose path to simple but equivalent path

paths = [
    "user/kai/files/temp.txt",
    "user/kai///files/./temp.txt",
    "user/kai/./files/temp.txt",
    "user/kai/files/../files/temp.txt",
]

for path in paths:
    print("{!r:>36} : {!r}".format(path, os.path.normpath(path)))

# abspath() convert a relative path to an absolute filename
#

# os.chdir("/home/kai")
PATHS = [
    ".",
    "..",
    "./one/two/three",
    "../one/two/three",
]

for path in PATHS:
    print("{!r:>21} : {!r}".format(path, os.path.abspath(path)))


# ------------------------------------------------------------------------------
# File Times
# os.path includes functions for retrieving file properties, similar to the
# ones returned by os.stat()

print("File:        ", __file__)
print("Access time  :", time.ctime(os.path.getatime(__file__)))
print("Modified time:", time.ctime(os.path.getmtime(__file__)))
print("Change time  :", time.ctime(os.path.getctime(__file__)))
print("Size         :", os.path.getsize(__file__))


# ------------------------------------------------------------------------------
# Testing Files
# When a program encounters a path name, it often needs to know whether the
# path refers to a file, directory, or symlink and whether it exists.

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    "/",
    "./broken_link",
]

for file in FILENAMES:
    print("File         : {!r}".format(file))
    print("Absolute     :", os.path.isabs(file))
    print("Is File?     :", os.path.isfile(file))
    print("Is Dir?      :", os.path.isdir(file))
    print("Is Link?     :", os.path.islink(file))
    print("Mountpoint   :", os.path.ismount(file))
    print("Exists?      :", os.path.exists(file))
    print("Link Exists? :", os.path.lexists(file))
    print()
