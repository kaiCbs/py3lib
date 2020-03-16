# functools: Tools for Manipulating Functions
# The functools module provides tools for adapting or extending functions and
# other callable objects, without completely rewriting them

import functools
from operator import add

# ------------------------------------------------------------------------------
# Decorator
# The primary tool supplied by the functools module is the class partial, which
# can be used to "wrap" a callable object with default arguments.


def pow(x, n):
    """power of a number"""
    return x ** n


pow2 = functools.partial(pow, n=2)
print(pow2(11))

# The partial object does not have __name__ or __doc__ attributes by default,
# and without those attributes, decorated functions are more difficult to debug.
# update_wrapper() can be used to copy or add attributes from the original
# function to the partial object.

print("__name__" in dir(pow2), "__doc__" in dir(pow2))
print(pow2.__doc__)

functools.update_wrapper(pow2, pow)

print("__name__" in dir(pow2), "__doc__" in dir(pow2))
print(pow2.__name__, pow2.__doc__, pow2.__doc__)


# Partials work with any callable object, not just with stand-alone functions.
# While partial() returns a callable ready to be used directly, partialmethod()
# returns a callable ready to be used as an unbound method of an object.


def standalone(self, a=1, b=2):
    "Standalone function"
    print(" called standalone with:", (self, a, b))


class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = "instance attribute"

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()
o.method1()
o.method2("Mice")

# Updating the properties of a wrapped callable is especially useful for
# decorators, because the transformed function ends up with properties of the
# original “bare” function.
# functools provides a decorator, wraps(), that applies update_wrapper() to the
# decorated function.


def simple_decorator(func, n_):
    @functools.wraps(func)
    def decorated(x, n=n_):
        print("Decorated with n =", (n))
        return func(x, n=n)

    return decorated


def show(func):
    print(func.__name__ + ":", func.__doc__)


show(pow)

pow2 = simple_decorator(pow, 3)
show(pow2)


# ------------------------------------------------------------------------------
# Decorator
# Python 2.1 introduced the rich comparison methods API (__lt__(), __le__(),
# __eq__(), __ne__(), __gt__(), and __ge__()), which perform a single
# comparison operation and return a boolean value. Python 3 deprecated
# __cmp__() in favor of these new methods,and functools provides tools to make
# it easier to write classes that comply with the new comparison requirements
# in Python 3.

# The rich comparison API is designed to allow classes with complex comparisons
# to implement each test in the most efficient way possible. The
# total_ordering() class decorator takes a class that provides some of the
# methods, and adds the rest of them.


@functools.total_ordering
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vec(%.1f, %.1f)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x ** 2 + self.y ** 2 == other.x ** 2 + other.y ** 2

    def __gt__(self, other):
        return self.x ** 2 + self.y ** 2 > other.x ** 2 + other.y ** 2


a = Vector(3, 4)
b = Vector(-4, 2)
c = Vector(0, 5)
print("|%s| < |%s|:" % (a, b), a < b)
print("|%s| = |%s|:" % (a, c), a == c)

# Since old-style comparison functions are deprecated in Python 3, the cmp
# argument to functions like sort() is also no longer supported. Older programs
# that use comparison functions can use cmp_to_key() to convert them to a
# function that returns a collation key, which is used to determine the
# position in the final sequence.

# Example: Leetcode 179. Largest Number
#
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         def compare_obj(a, b):
#             cmp = int(a + b) - int(b + a)
#             return (cmp < 0) + (cmp <= 0) - 1

#         get_key = functools.cmp_to_key(compare_obj)
#         nums = map(str, nums)
#         return str(int("".join(sorted(nums, key=get_key))))


# ------------------------------------------------------------------------------
# Caching
# The lru_cache decorator wraps a function in a "least recently used" cache.
# Arguments to the function are used to build a hash key, which is then mapped
# to the result. Subsequent calls with the same arguments will fetch the value
# from the cache instead of calling the function.

# To prevent the cache from growing without bounds in a long-running process,
# it is given a maximum size. The default is 128 entries, but that size can be
# changed for each cache using the maxsize argument


# ------------------------------------------------------------------------------
# Reducing a Data Set
# The reduce() function takes a callable and a sequence of data as input. It
# produces a single value as output based on invoking the callable with the
# values from the sequence and accumulating the resulting output

print(functools.reduce(add, range(1, 101)))


# ------------------------------------------------------------------------------
# Generic Functions
# In a dynamically typed language like Python, there is often a need to perform
# slightly different operations based on the type of an argument, especially
# when dealing with the difference between a list of items and a single item.
# It is simple enough to check the type of an argument directly, but in cases
# where the behavioral difference can be isolated into separate functions,
# functools provides the singledispatch() decorator to register a set of
# generic functions for automatic switching based on the type of the first
# argument to a function.


@functools.singledispatch
def func(arg):
    pass


@func.register(int)
def func_int(x):
    print("Dealing with Int:", x)


@func.register(list)
def func_list(x):
    print("Dealing with List:", x)


func(12)
func([1, 2, 3])
