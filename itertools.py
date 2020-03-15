# itertools: Iterator Functions
# The itertoools module includes a set of functions for working with sequence
# data sets. The functions provided are inspired by similar features of
# functional programming languages such as Clojure, Haskell, APL, and SML.

import itertools


# ------------------------------------------------------------------------------
# The chain() function takes several iterators as arguments and and returns a
# single iterator that produces the contents of all of the inputs as though they
# came from a single iterator

for i in itertools.chain(list("hello"), list(" world!")):
    print(i, end="")

# The chain.from_iterable() can be used to construct the chain if the iterables
# are combined in a lazy way

iterables = ([1, 2, 3], [4, 5, 6])

for i in itertools.chain.from_iterable(iterables):
    print(i, end="")

# Built-in function zip() stops when the first input iterator is exhausted, but
# the zip_longest() substitutes None for any missing values

array1 = range(10)
array2 = range(5)

print(list(zip(array1, array2)))
print(list(itertools.zip_longest(array1, array2)))
