# pathlib: File System Paths
# The pathlib module provides an object-oriented API for parsing, building,
# testing, and otherwise working on filenames and paths, instead of using
# low-level string operations.

import pathlib
import sys
import time

# ------------------------------------------------------------------------------
# Path Representations
# “pure” classes, which operate on strings but do not interact with an actual
# file system
# “concrete” classes, which extend the API to include operations that reflect
# or modify data on the local file system.
# The pure classes PurePosixPath and PureWindowsPath can be instantiated and
# used on any operating system, since they work only on names. To instantiate
# the correct class for working with a real file system, use Path to get either
# a PosixPath or a WindowsPath, depending on the platform.

# ------------------------------------------------------------------------------
# Building Paths
# To create a new path referring to a value relative to an existing path, use
# the / operator to extend the path

usr = pathlib.PurePosixPath("/home/kai/")
print(usr)
usr_local = usr / "local"
print(usr_local)
usr_share = usr / pathlib.PurePosixPath("share")
print(usr_share)
root = usr / ".."
print(root)
etc = root / "/etc"  # start with /
print(etc)

# The concrete path classes include a resolve() method for normalizing a path
# by looking at the file system for directories and symbolic links and
# producing the absolute path referred to by a name

usr_local = pathlib.Path("/home/kai/local")

share = usr_local / ".." / "share"

print(share)
print(share.resolve())

# use joinpath() to join segments

root = pathlib.PurePosixPath("/home/")
subdirs = ["kai", "local"]
usr_local = root.joinpath(*subdirs)
print(usr_local)

# use with_name() to create a new path that replaces the name portion of a path
# with a different filename

ind = pathlib.PurePosixPath("source/pathlib/index.rst")
print(ind)
py = ind.with_name("pathlib_from_existing.py")
print(py)
pyc = py.with_suffix(".pyc")
print(pyc)

# ------------------------------------------------------------------------------
# Parsing Paths

print(ind.parts)
print(list(ind.parents))

print("path : {}".format(py))
print("name : {}".format(py.name))
print("suffix: {}".format(py.suffix))
print("stem : {}".format(py.stem))

# ------------------------------------------------------------------------------
# Creating Concrete Paths

home = pathlib.Path.home()
print("home: ", home)
cwd = pathlib.Path.cwd()
print("cwd : ", cwd)

# ------------------------------------------------------------------------------
# Directory Contents
code = pathlib.Path.cwd().joinpath("code")
for f in code.iterdir():
    print(f)

print(" - - ")
for f in code.glob("c*.py"):
    print(f)

# ------------------------------------------------------------------------------
# Reading and Writing Files
# For immediately retrieving the contents, use read_bytes() or read_text() .
# To write to the file, use write_bytes() or write_text(). Use the open()
# method to open the file and retain the file handle, instead of passing the
# name to the built-in open() function

import pathlib

f = pathlib.Path("tempfile.txt")
print(f)
f.write_bytes("This is the Content".encode("utf-8"))
with f.open("r", encoding="utf-8") as file:
    print("read from open(): {!r}".format(file.read()))

print("read_text(): {!r}".format(f.read_text("utf-8")))

# ------------------------------------------------------------------------------
# Manipulating Directories and Symbolic Links
# Use mkdir() to create paths that do not exist. If the path already exists,
# mkdir() raises a FileExistsError.

p = pathlib.Path("example_dir")
print("Creating {}".format(p))
p.mkdir()

# TODO: symbolic links

# ------------------------------------------------------------------------------
# File Types
# TODO: finish later

# ------------------------------------------------------------------------------
# File Properties

p = pathlib.Path(__file__)
print("{} is owned by {}/{}".format(p, p.owner(), p.group()))

stat_info = p.stat()
print(" Size:", stat_info.st_size)
print(" Permissions:", oct(stat_info.st_mode))
print(" Owner:", stat_info.st_uid)
print(" Device:", stat_info.st_dev)
print(" Created:", time.ctime(stat_info.st_ctime))
print(" Last modified:", time.ctime(stat_info.st_mtime))
print(" Last accessed:", time.ctime(stat_info.st_atime))


# The touch() method works like the Unix command touch to create a file or
# update an existing file’s modification time and permissions.

t = pathlib.Path("touched")
if t.exists():
    print("already exists")
else:
    print("creating new")
t.touch()
start = t.stat()
time.sleep(1)
t.touch()
end = t.stat()
print("Start:", time.ctime(start.st_mtime))
print("End :", time.ctime(end.st_mtime))


# ------------------------------------------------------------------------------
# Permissions
# On Unix-like systems, file permissions can be changed using chmod, passing
# the mode as an integer. Mode values can be constructed using constants
# defined in the stat module. This example toggles the user’s execute
# permission bit.

# TODO: later


# ------------------------------------------------------------------------------
# Deleting
# To remove an empty directory, use rmdir()

p = pathlib.Path("example_dir")
p.rmdir()

# For files, symbolic links, and most other path types, use unlink()

t.unlink()
