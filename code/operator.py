# operator: Functional Interface to Built-In Operators
# Programming using iterators occasionally requires creating small functions
# for simple expressions

import operator

# ------------------------------------------------------------------------------
# Logical Operations
# Functions are provided for determining the boolean equivalent for a value,
# negating a value to create the opposite boolean value, and comparing objects
# to see if they are identical.

a, b, c = [1], [1], [-1]

print("not a:       ", operator.not_(a))
print("if a:        ", operator.truth(a))
print("b is a:      ", operator.is_(a, b))
print("b is not a:  ", operator.is_not(a, b))


# ------------------------------------------------------------------------------
# Comparison Operators
# All of the rich comparison operators are supported

a, b = 1, 5.0

print("a = ", a)

for func in "lt le eq ne ge gt".split():
    print("{}(a, b): {}".format(func, getattr(operator, func)(a, b)))


# ------------------------------------------------------------------------------
# Arithmetic Operators
# The arithmetic operator for manipulating numerical values are also supported.
a, b, c, d = -1, 5.0, 2, 6

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("\nPositive/Negative:")
print("abs(a):", operator.abs(a))
print("neg(a):", operator.neg(a))
print("neg(b):", operator.neg(b))
print("pos(a):", operator.pos(a))
print("pos(b):", operator.pos(b))
print("\nArithmetic:")
print("add(a, b) :", operator.add(a, b))
print("floordiv(a, b):", operator.floordiv(a, b))
print("floordiv(d, c):", operator.floordiv(d, c))
print("mod(a, b) :", operator.mod(a, b))
print("mul(a, b) :", operator.mul(a, b))
print("pow(c, d) :", operator.pow(c, d))
print("sub(b, a) :", operator.sub(b, a))
print("truediv(a, b) :", operator.truediv(a, b))
print("truediv(d, c) :", operator.truediv(d, c))
print("\nBitwise:")
print("and_(c, d) :", operator.and_(c, d))
print("invert(c) :", operator.invert(c))
print("lshift(c, d):", operator.lshift(c, d))
print("or_(c, d) :", operator.or_(c, d))
print("rshift(d, c):", operator.rshift(d, c))

# ------------------------------------------------------------------------------
# Sequence Operators
# The operatirs for working with sequence can be organized into four groups:
# building up sequences, searching for items, accessing contents, and removing
# items from sequences.

a = [1, 2, 3]
b = ["a", "b", "c"]
print("a =", a)
print("b =", b)


print("\nConstructive:")
print(" concat(a, b):", operator.concat(a, b))
print("\nSearching:")
print(" contains(a, 1) :", operator.contains(a, 1))
print(' contains(b, "d"):', operator.contains(b, "d"))
print(" countOf(a, 1) :", operator.countOf(a, 1))
print(' countOf(b, "d") :', operator.countOf(b, "d"))
print(" indexOf(a, 5) :", operator.indexOf(a, 1))

print("\nAccess Items:")
print(" getitem(b, 1) :", operator.getitem(b, 1))
print(" getitem(b, slice(1, 3)) :", operator.getitem(b, slice(1, 3)))
print(' setitem(b, 1, "d") :', end=" ")
operator.setitem(b, 1, "d")
print(b)
print(" setitem(a, slice(1, 3), [4, 5]):", end=" ")
operator.setitem(a, slice(1, 3), [4, 5])
print(a)

print("\nDestructive:")
print(" delitem(b, 1) :", end=" ")
operator.delitem(b, 1)
print(b)
print(" delitem(a, slice(1, 3)):", end=" ")
operator.delitem(a, slice(1, 3))
print(a)


# ------------------------------------------------------------------------------
# In-Place Operators
# In addition to the standard operators, many types of objects support
# "inplace" modification through special operators such as +=.


c = [1, 2, 3]
d = ["a", "b", "c"]
print("c =", c)
print("d =", d)

operator.iadd(c, d)
print("iadd(c, d) => c =", c)


# ------------------------------------------------------------------------------
# Attribute and Item "Getters"
# One of the most unusual features of the operator module is the concept of
# getters. These callable objects are constructed at runtime and retrieve
# attributes of objects or contents from sequences.

getName = operator.attrgetter("__name__")
print([getName(func) for func in (abs, max, min, dict)])

# Item getters work like lambda x,y=5: x[y]

getItem = operator.itemgetter("val")
array = [{"val": -i} for i in range(4)]
vals = [getItem(i) for i in array]
print(" values:", vals)
print(" sorted:", sorted(array, key=getItem))

getSecond = operator.itemgetter(1)
print(getSecond("abcde"), getSecond([1, 2, 3, 4]))


# ------------------------------------------------------------------------------
# Combining Operators and Custom Classes
# The functions in the operator module work via the standard Python interfaces
# when performing their operations. Thus, they work with user-defined classes
# as well as the built-in types.
