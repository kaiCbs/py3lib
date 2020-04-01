# shutil: High-Level File Operation
# The shutil module includes high-level file operations such as copying and
# archiving

import shutil
import glob
import io
import os
import sys

# ------------------------------------------------------------------------------
# Copy files
# copyfile() copies th econtents of the source to the destination. It raises
# IOError if it doesn't have permission to write to the destination file.
# The implementation of copyfile uses the lower-level function copyfileobj().
# While the arguments to copyfile() are filenames, the arguments to
# copyfileobj() are open file handles.

print("Before:", glob.glob("code/c*"))
shutil.copyfile("code/contextlib.py", "code/contextlib.py.copy")
print("After:", glob.glob("code/c*"))


class VerboseStringIO(io.StringIO):
    def read(self, n=-1):
        next = io.StringIO.read(self, n)
        print("read({}) got {} bytes".format(n, len(next)))
        return next


text = """
copyfile() copies th econtents of the source to the destination. It raises
IOError if it doesn't have permission to write to the destination file.
The implementation of copyfile uses the lower-level function copyfileobj().
While the arguments to copyfile() are filenames, the arguments to
copyfileobj() are open file handles.
"""

print("Default:")
input = VerboseStringIO(text)
output = io.StringIO()
shutil.copyfileobj(input, output)

print("\nAll at once:")
input = VerboseStringIO(text)
output = io.StringIO()
shutil.copyfileobj(input, output, -1)

print("\nBlocks of 256:")
input = VerboseStringIO(text)
output = io.StringIO()
shutil.copyfileobj(input, output, 256)

# copy() function interprets the output name in the same way that Unix command
# line tool cp does.
# copy2() works like copy(), but includes the access and modification times in
# the meta-data copied to the new file.


# os.mkdir("example")
print("Before:", glob.glob("example/*"))
shutil.copy("code/contextlib.py.copy", "example")
print("Before:", glob.glob("example/*"))


# ------------------------------------------------------------------------------
# Copy File Metadata
# To copy the permissions from one file to another, use copymode().

with open("file_test.txt", "wt") as f:
    f.write("This is a sentence.")
os.chmod("file_test.txt", 0o444)

print("BEFORE:", oct(os.stat("file_test.txt").st_mode))
shutil.copymode("code/contextlib.py", "file_test.txt")
print("AFTER :", oct(os.stat("file_test.txt").st_mode))

# To copy other metadata for the file, use copystat()


# ------------------------------------------------------------------------------
# Working with Directory Trees
# shutil includes three functions for working with directory trees.
# To copy a directory from one place to another, use copytree()


os.unlink("code/contextlib.py.copy")
