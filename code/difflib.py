# difflib: Compare Sequences
# The difflib module contains tools for computing and working with differences between sequences.
# It is especially useful for comparing text, and includes functions that produce reports using
# several common difference formats

import difflib


# ----------------------------------
# Comparing Bodies of Text
# The Differ class works on sequences of text lines and produces human-readable deltas, or
# change instructions, including differences within individual lines. The default output
# produced by Differ is similar to the diff command-line tool under Unix. It includes the
# original input values from both lists, including common values, and markup data to indicate
#
# which changes were made.

text_correct = """
Bloomberg, who will be on the ballot Tuesday for the first time this primary season, made the 
comments amid new turmoil in the presidential contest. With rivals Pete Buttigieg and Amy Klobuchar 
now abruptly out, Joe Biden has consolidated support among establishment Democrats hoping to 
present a more centrist alternative to democratic socialist Bernie Sanders.
""".splitlines()

text_wrong = """
Bloomberg, who will be on the ballot tuesday for the first time this primary season, mdae the 
comments  amid enw tuomiol in the presidential contest. With rivals Pete Buttigieg and amy Klobuchar
now abruptly out, Joe Biden has consolidated support among establishment Democrats hoping to 
present a more centrist altenative to democratic socialist bernie sanders.
""".splitlines()

checker = difflib.Differ()
diff = checker.compare(text_correct, text_wrong)
print("\n".join(diff))

# - Bloomberg, who will be on the ballot Tuesday for the first time this primary season, made the
# ?                                      ^                                                 -

# + Bloomberg, who will be on the ballot tuesday for the first time this primary season, mdae the
# ?                                      ^                                                +

# - comments amid new turmoil in the presidential contest. With rivals Pete Buttigieg and Amy Klobuchar
# ?                -    ^  -                                                              ^            -

# + comments  amid enw tuomiol in the presidential contest. With rivals Pete Buttigieg and amy Klobuchar
# ?          +     +     ^ +                                                               ^

#   now abruptly out, Joe Biden has consolidated support among establishment Democrats hoping to
# - present a more centrist alternative to democratic socialist Bernie Sanders.
# ?                             -                               ^      ^

# + present a more centrist altenative to democratic socialist bernie sanders.
# ?                                                            ^      ^


# ----------------------------------
# Other Formats
# While the Differ class shows all of the input lines, a unified diff includes only the modified lines
# and a bit of context. The unified_diff() function produces this sort of output.

diff = difflib.unified_diff(text_wrong, text_correct, lineterm="",)
print("\n".join(list(diff)))


# ----------------------------------
# Junk Data
# The default for Differ is to not ignore any lines or characters explicitly, but rather to rely on
# the ability of SequenceMatcher to detect noise. The default for ndiff() is to ignore space and tab characters.

from difflib import SequenceMatcher

a, b = "AA--", "A--A"

print("\nWithout junk detection:")
s = SequenceMatcher(None, a, b)
for block in s.get_matching_blocks():
    i, j, k = block
    print("a[%d] and b[%d] match for %d elements" % block, a[i : i + k])

print('\nTreat "-" as junk:')
s = SequenceMatcher(lambda x: x == "-", a, b)
for block in s.get_matching_blocks():
    i, j, k = block
    print("a[%d] and b[%d] match for %d elements" % block, a[i : i + k])


# ----------------------------------
# Comparing Arbitrary Types
# The SequenceMatcher class compares two sequences of any types, as long as the values are hashable.
# It uses an algorithm to identify the longest contiguous matching blocks from the sequences,
# eliminating “junk” values that do not contribute to the real data. The funct get_opcodes() returns
# a list of instructions for modifying the first sequence to make it match the second.
# difflib.get_opcodes() Instructions
#
#  'replace'    Replace a[i1:i2] with b[j1:j2].
#  'delete'     Remove a[i1:i2] entirely.
#  'insert'     Insert b[j1:j2] at a[i1:i1].
#  'equal'      The subsequences are already equal.

seq1 = [1, 3, 5, 7, 9, 11]
seq2 = [2, 3, 5, 7, 11, 13]

match = difflib.SequenceMatcher(None, seq1, seq2)
for op in match.get_opcodes():
    print("Action:", op[0], "%s with %s" % (seq1[op[1] : op[2]], seq2[op[3] : op[4]]))

