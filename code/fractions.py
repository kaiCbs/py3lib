# fractions: Rational Numbers
# The Fraction class implements numerical operations for rational number based
# on API defined by Rational in the numbers module.

import fractions

for n, d in zip(range(1, 6), range(5, 10)):
    f = fractions.Fraction(n, d)
    print("{}/{} = {}".format(n, d, f))

# we can also creates a new context using string represenation

for frac in "1/2 2/6 5/15".split():
    f = fractions.Fraction(frac)
    print("{} = {}".format(frac, f))

# we can even pass float to construct a fraction

for frac in "0.5 0.375 0.36 0.85".split():
    f = fractions.Fraction(frac)
    print("{0:>5} = {1}".format(frac, f))

# Floating-point values can't be expressed exactly may yield unexpected results
# convert to string first or use Decimal representations


# ------------------------------------------------------------------------------
# Arithmetic
# fractions can be used to do calculation

frac1 = fractions.Fraction(3, 7)
frac2 = fractions.Fraction(2, 5)
print("{} + {} = {}".format(frac1, frac2, frac1 + frac2))
print("{} - {} = {}".format(frac1, frac2, frac1 - frac2))
print("{} * {} = {}".format(frac1, frac2, frac1 * frac2))
print("{} / {} = {}".format(frac1, frac2, frac1 / frac2))


# ------------------------------------------------------------------------------
# Approximation
# Fraction can convert a floating-point number to an approximate rational value

import fractions
import math

print("PI =", math.pi)
pi = fractions.Fraction(str(math.pi))
print("No limit =", pi)
for i in [1, 6, 11, 60, 70, 90, 100]:
    limited = pi.limit_denominator(i)
    print("{0:8} = {1}".format(i, limited))
