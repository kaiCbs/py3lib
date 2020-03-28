# random: Pseudorandom Number Generators
# The random module provides a fast pseudorandom number generator based on the
# Mersenne Twister algorithm.

import random

random.seed(1)

# ------------------------------------------------------------------------------
# Generating Random Numbers
# random() returns a flaot within the range 0 <= n < 1.0

print("random():", random.random())

# use uniform() to specify a range

print("uniform(0, 10):", random.uniform(0, 10))


# ------------------------------------------------------------------------------
# Saving State
# The internal state of the pseudorandom algorithm used by random() can be
# saved and used to control the numbers produced in subsequent runs.

# TODO: finish later


# ------------------------------------------------------------------------------
# Random Integers
# Use randint() to generate integers

print("randint(-5, 5):", random.randint(-5, 5))


# ------------------------------------------------------------------------------
# Picking Random Items
# choice() function makes a random selection from a sequence.

students = ["Bob", "Tom", "Mike", "Alice", "Jenny"]

print(random.choice(students))

# ------------------------------------------------------------------------------
# reorder sequence
# shuffle() will shuffile a list in place

print("student list : {}".format(students))
random.shuffle(students)
print("shuffled list: {}".format(students))

# ------------------------------------------------------------------------------
# sampling
# sample() generates samples without repeating values and without modifying the
# input sequence.

print("Random 3 students: {}".format(random.sample(students, 3)))


# ------------------------------------------------------------------------------
# Multiple Simultaneous Generators
# In addition to module-level functions, random includes a Random class to
# manage the internal state for several random number generators. All of the
# functions described earlier are available as methods of the Random instances,
# and each instance can be initialized and used separately, without interfering
# with the values returned by other instances.

r1 = random.Random()
r2 = random.Random()

print("Independent generator:")
for i in range(5):
    print("  {:.5f},{:.5f}".format(r1.random(), r2.random()))

r1.seed(1)
r2.seed(1)

print("With same seed:")
for i in range(5):
    print("  {:.5f},{:.5f}".format(r1.random(), r2.random()))


# ------------------------------------------------------------------------------
# SystemRandom
# Some operating systems provide a random number generator that has access to
# more sources of entropy that can be introduced into the generator. random
# exposes this feature through the SystemRandom class. It has the same API as
# Random but uses os.urandom() to generate the values that form the basis of
# all the other algorithms.

r1 = random.SystemRandom()
r2 = random.SystemRandom()

print("Independent generator:")
for i in range(5):
    print("  {:.5f},{:.5f}".format(r1.random(), r2.random()))


# ------------------------------------------------------------------------------
# Other Distribution
# TODO: add other ditributions
