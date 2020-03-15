# itertools: Iterator Functions
# The itertoools module includes a set of functions for working with sequence
# data sets. The functions provided are inspired by similar features of
# functional programming languages such as Clojure, Haskell, APL, and SML.

import itertools


# ------------------------------------------------------------------------------
# The chain() function takes several iterators as arguments and and returns a
# single iterator that produces the contents of all of the inputs as though
# they came from a single iterator

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

print("\nzip\n", list(zip(array1, array2)))
print("\nzip_longest\n", list(itertools.zip_longest(array1, array2)))

# islice() function returns an iterator that returns selected items from the
# input iterator, by index

print("\n\nStop at 10:")
for i in itertools.islice(range(50), 10):
    print(i, end=" ")

print("\n\nStart at 5, Stop at 15:")
for i in itertools.islice(range(50), 5, 15):
    print(i, end=" ")

print("\n\nStep = 3")
for i in itertools.islice(range(50), 0, 50, 3):
    print(i, end=" ")

# tee() function returns several independent iterators based on a single
# original input.

r = itertools.islice(itertools.count(), 5)
i1, i2 = itertools.tee(r)

print("\ni1:", list(i1))
print("i2:", list(i2))

# The new iterators created by tee() share their input

r = itertools.islice(itertools.count(), 5)
i1, i2 = itertools.tee(r)
print("r:")
for i in r:
    print(i, end=" ")
    if i > 1:
        break

print("\ni1:", list(i1))
print("i2:", list(i2))

# If values are consumed from the original input, the new iterators will not
# produce those values.


# ------------------------------------------------------------------------------
# Converting Inputs
# The built-in map() function returns an iterator that calls a function on the
# values in the input iterators, and returns the results. It stops when any
# input iterator is exhausted. The starmap() function is similar to map(), but
# but instead of constructing a tuple from multiple iterators, it splits up the
# items in a single iterator as arguments to the mapping function using the *


def multiply(x, y):
    return x, y, x * y


for result in map(multiply, range(5), range(10, 15)):
    print("%d * %d = %d" % result)

for result in itertools.starmap(multiply, zip(range(5), range(10, 15))):
    print("%d * %d = %d" % result)


# ------------------------------------------------------------------------------
# Producing New Values
# The count() function returns an iterator that produces consecutive integers.
# The first number can be passed as an argument (the default is zero). There is
# no upper bound argument.

for i in zip(itertools.count(1), "abcdfe"):
    print(i)

# The cycle() function returns an iterator that repeats the contents of the
# arguments it is given indefinitely.

for i in zip(range(10), itertools.cycle(["Hello", "world!"])):
    print(i)

# The repeat() function returns an iterator that produces the same value each
# time it is accessed.

for i in itertools.repeat("Hello world!", 5):
    print(i)


# ------------------------------------------------------------------------------
# Filtering
# The dropwhile() function returns an iterator that produces elements of the
# input iterator after a condition becomes false for the first time.

print("Dropwhile:")
for i in itertools.dropwhile(lambda x: x < 4, [1, 3, 5, 7, 9, 12]):
    print(i)

# The opposite of dropwhile() is takewhile(). It returns an iterator that
# itself returns items from the input iterator as long as the test function
# returns true.

print("Takewhile:")
for i in itertools.takewhile(lambda x: x < 10, [1, 3, 5, 7, 9, 12]):
    print(i)


# The built-in function filter() returns an iterator that includes only items
# for which the test function returns true. The filterfalse() returns an
# iterator that includes only items where the test function returns false.

print("Filter:")
for i in filter(lambda x: x < 10, [11, 3, 52, 7, 9, 12]):
    print(i)

print("Filterfalse:")
for i in itertools.filterfalse(lambda x: x < 10, [11, 3, 52, 7, 9, 12]):
    print(i)

# compress() offers another way to filter the contents of an iterable. Instead
# of calling a function, it uses the values in another iterable to indicate
# when to accept a value and when to ignore it.

print("Compress:")
data = [11, 3, 52, 7, 9, 12]
for i in itertools.compress(data, [n > 10 for n in data]):
    print(i)


# ------------------------------------------------------------------------------
# Grouping Data
# The groupby() function returns na iterator that produces sets of values
# organized by a common key. The input sequence needs to be sorted on the key
# value so that the groupings will work out as expected.

data = [["a", 1], ["a", 5], ["b", 4], ["c", 3], ["c", 2], ["c", 3]]
for k, g in itertools.groupby(data, lambda x: x[0]):
    print(k, list(g))

# ------------------------------------------------------------------------------
# Combining Inputs
# The accumulate() function process the input iterable, passing the nth and
# n+1st item to a function and producing the return value instead of either
# input.


print(list(itertools.accumulate(range(1, 6))))
print(list(itertools.accumulate(range(1, 6), func=lambda x, y: x * y)))
print(list(itertools.accumulate("abcde")))

# Nested for loops that iterate over multiple sequences can often be replaced
# with product(), which produces a single iterable whose values are the
# Cartesian product of the set of input values.

title = ["A", "B", "C"]
num = [1, 2, 3, 4, 5, 6]
print(list(itertools.product(title, num)))


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=" ")
        if (i % 3) == 0:
            print()


print("Repeat 2:")
show(list(itertools.product(range(3), repeat=2)))
print("Repeat 3:")
show(list(itertools.product(range(3), repeat=3)))

# The permutations() function produces items from the input iterable combined
# in the possible permutations of the given length. It defaults to producing
# the full set of all permutations. To limit the values to unique combinations
# rather than permutations, use combinations().


def show(iterable):
    return ["".join(i) for i in iterable]


print(show(itertools.permutations("abcd")))
print(show(itertools.combinations("abcd", r=3)))
