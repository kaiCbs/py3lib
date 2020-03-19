# os.path: Platform-Independent Manipulation of Filenames


import os.path

paths = [
    "user/kai/files/temp.txt",
    "user/kai/files/",
    "user/kai/files",
    "user/kaifiles",
]

for path in paths:
    print("{!r:>25} : {}".format(path, os.path.split(path)))


print(os.path.curdir, os.path.pardir, os.path.sep, os.path.extsep)

print("PREFIX:", os.path.commonprefix(paths))

print("PREFIX:", os.path.commonpath(paths))

for user in ["", "kai", "unknown"]:
    lookup = "~" + user
    print("{!r:>15} : {!r}".format(lookup, os.path.expanduser(lookup)))

    #         '~' : 'C:\\Users\\xkism'
    #      '~kai' : 'C:\\Users\\kai'
    #  '~unknown' : 'C:\\Users\\unknown'
