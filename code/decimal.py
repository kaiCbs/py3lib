# decimal: Fixed- and Floating-Point Math
# The decimal module implements fixed- and floating-point arithmetic
# using the model familiar to most people.

import decimal


# ------------------------------------------------------------------------------
# Decimal
# Decimal values are represented as instance of the Decimal class.

fmt = "{0:<25} {1:<25}"

print(fmt.format("Input", "Output"))
print(fmt.format(5, decimal.Decimal(5)))
print(fmt.format("3.14", decimal.Decimal("3.14")))

f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print("{:<25} {:<25}".format(f, str(decimal.Decimal.from_float(f))[:25]))


# ------------------------------------------------------------------------------
# Formatting
# Decimal responds to Python's string formatting protocol by using the same
# syntax and options as other numerical types

d = decimal.Decimal(1.01)
print("Precision:")
print("{:.1}".format(d))
print("{:.2}".format(d))
print("{:.3}".format(d))
print("{:.18}".format(d))
print("\nWidth and precision combined:")
print("{:5.1f} {:5.1g}".format(d, d))
print("{:5.2f} {:5.2g}".format(d, d))
print("{:5.2f} {:5.2g}".format(d, d))
print("\nZero padding:")
print("{:05.1}".format(d))
print("{:05.2}".format(d))
print("{:05.3}".format(d))

# ------------------------------------------------------------------------------
# Arithmetic
# Decimal overloads the simple arithmetic operators so instances can be
# manipulated in much the same way as the built-in numeric types.
# Decimal operators also accept integer arguments. In contrast, floating-point
# values must be converted to Decimal instances before they can be used by
# these operators.
a = decimal.Decimal("1.1")
b = decimal.Decimal("3.3")
c = 1
d = 3

print(a / b)
print(a / d)
print(c / b)
print(c / d)


# ------------------------------------------------------------------------------
# Special Values
# In addition to the expected numerical values, Decimal can represent several
# special values, including positive and negative values for infinity, “not a
# number” (NaN), and zero.

for value in ["Infinity", "NaN", "0"]:
    print(decimal.Decimal(value), decimal.Decimal(value))
    print()


# ------------------------------------------------------------------------------
# Context
# It is possible to override settings such as the precision maintained, the way
# in which rounding is performed, and error handling by using a context.
# Contexts can be applied for all Decimal instances in a thread or small local
# code region. To retrieve the current global context, use getcontext().

import decimal

context = decimal.getcontext()
print("Emax =", context.Emax)
print("Emin =", context.Emin)
print("capitals =", context.capitals)
print("prec =", context.prec)
print("rounding =", context.rounding)
print("flags =")
for f, v in context.flags.items():
    print(" {}: {}".format(f, v))
print("traps =")
for t, v in context.traps.items():
    print(" {}: {}".format(t, v))


# The prec attribute of the context controls the precision maintained for new
# values created as a result of arithmetic. Literal values are maintained as
# described.


d = decimal.Decimal("0.123456789")
for i in [1, 3, 6, 9, 6, 4, 2]:
    decimal.getcontext().prec = i
    print("%d:" % i, d, d * 1)

# TODO: rounding, thread, local context
