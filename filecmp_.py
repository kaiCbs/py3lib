# filecmp: Compare Files
# The filecmp module includes functions and a class for comparing files
# and directories and on the file system.

import os
import filecmp


def make_file(filename, body=None):
    with open(filename, "w") as f:
        f.write(body or filename)
    return


def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)
    os.mkdir("dir1")
    os.mkdir("dir2")
