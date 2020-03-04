# collections: Container Data Types
# The collections module includes container data types beyond the built-in types list, dict, and tuple.

import collections


# ----------------------------------
# ChainMap: Search Multiple Dictionaries
# The ChainMap class manages a sequence of dictionaries, and searches through them in the order they appear 
# to find values associated with keys. A ChainMap makes a good “context” container, since it can be treated 
# as a stack for which changes happen as the stack grows, with these changes being discarded again as the 
# stack shrinks.

a = {"First": "Tom", "Second": "Jimmy"}
b = {"Third": "Alice", "First": "Tony"}
c = {"Fourth": "Mike", "Second": "Mary"}

rank = collections.ChainMap(a,b,c)

for key in rank:
    print("%s\t%s"%(key, rank[key]))

print(rank.maps)

# A ChainMap does not cache the values in the child mappings. Thus, if their contents are modified, the results 
# are reflected when the ChainMap is accessed.

a["First"] = "Mike"

for key in rank:
    print("%s\t%s"%(key, rank[key]))

# It is also possible to set values through the ChainMap directly, although only the first mapping in 
# the chain is actually modified.

rank["First"] = "Bob"
print(a["First"], b["First"])

# When we use Chain map

# 1. More information: since a ChainMap structure is "layered", it supports answering question like: Am I 
# getting the "default" value, or an overridden one? What is the original ("default") value? At what level 
# did the value get overridden (borrowing @b4hand's config example: user-config or command-line-overrides)? 
# Using a simple dict, the information needed for answering these questions is already lost.

# 2. Speed tradeoff: suppose you have N layers and at most M keys in each, constructing a ChainMap takes O(N) 
# and each lookup O(N) worst-case[*], while construction of a dict using an update-loop takes O(NM) and each 
# lookup O(1). This means that if you construct often and only perform a few lookups each time, or if M is big, 
# ChainMap's lazy-construction approach works in your favor.

# ----------------------------------
# Counter: Count Hashable Objects
# A Counter is a container that keeps track of how many times equivalent values are added. It can be used 
# to implement the same algorithms for which other languages commonly use bag or multiset data structures.

# Counter supports three forms of initialization. list, dict, keyword arguments.

print(collections.Counter([1,2,2,3,3,3,4,4,4,4]))
print(collections.Counter({1:1,2:2,3:3}))
print(collections.Counter(a=1,b=2,c=3)) 

# An empty Counter can be constructed with no arguments and populated via the update() method.

letters = collections.Counter()
letters.update("aabbbcccc")
print(letters)

# A counter's values can be retrieved using the dictionary API.
# The elements() method returns an iterator that produces all of the items known to the Counter.
# Use most_common() to get n most frequently encountered input values and their respective counts.

# Counter instances support arithmetic and set operations for aggregating results. This example 
# shows the standard operators for creating new Counter instances, but the in-place 
# operators +=, -=, &=, and |= are also supported.


# ----------------------------------
# defaultdict: Missing Keys Return a Default Value
# The standard dictionary includes the method setdefault() for retrieving a value and establishing 
# a default if the value does not exist. By contrast, defaultdict lets the caller specify the 
# default up front when the container is initialized. To create such a "default" item, it calls the 
# function object that you pass to the constructor (more precisely, it's an arbitrary "callable" 
# object, which includes function and type objects)

d = collections.defaultdict(int)
for l in "This is a document and this document has a owner and a keeper".split():
    d[l]+=1
print(d)


# ----------------------------------
# deque: Double-Ended Queue
# A double-ended queue, or deque, supports adding and removing elements from either end of the queue. 
# The more commonly used stacks and queues are degenerate forms of deques, where the inputs and 
# outputs are restricted to a single end.

d = collections.deque([7,11,13])

# A deque can be populated from either end, termed “left” and “right” in the Python implementation.
# The extendleft() function iterates over its input and performs the equivalent of an appendleft() 
# for each item. The end result is that the deque contains the input sequence in reverse order.

d.extend([17,19])
print(d)
d.append(23)
print(d)
d.extendleft([5,3])
print(d)
d.appendleft(2)
print(d)

# Similarly, the elements of the deque can be consumed from both ends or either end, depending 
# on the algorithm being applied. deques are thread-safe, the contents can even be consumed from 
# both ends at the same time from separate threads.

print(d.pop(), d.pop(), d.popleft())

# Another useful aspect of the deque is the ability to rotate it in either direction, so as to 
# skip over some items.

d.rotate(2)
print(d)

# A deque instance can be configured with a maximum length so that it never grows beyond that size. 
# When the queue reaches the specified length, existing items are discarded as new items are added. 
# This behavior is useful for finding the last n items in a stream of undetermined length.

d = collections.deque(maxlen=5)
for i in range(100):
    if i % 7 == 0:
        d.append(i)
print(d)


# ----------------------------------
# namedtuple: Tuple Subclass with Named Fields
# namedtuple instances are just as memory efficient as regular tuples because they do not have 
# per-instance dictionaries. Each kind of namedtuple is represented by its own class, which is 
# created by using the namedtuple() factory function. The arguments are the name of the new class 
# and a string containing the names of the elements.

# Field names are invalid if they are repeated or conflict with Python keywords.

Person = collections.namedtuple('Person', 'name age')
student = Person(name="Mike", age=20)
print(student)
print('{} is {} years old'.format(*student))
print('{} is {} years old'.format(student[0], student[1]))

# namedtuple provides several useful attributes and methods for working with subclasses and instances. 
# All of these built-in properties have names prefixed with an underscore (_), which by convention in 
# most Python programs indicates a private attribute. For namedtuple, however, the prefix is intended 
# to protect the name from collision with user-provided attribute names.

print("Fields: ", student._fields)
print("Fields: ", student._asdict())
student2 = student._replace(name="Bob")
print('{} is {} years old'.format(*student2))


# ----------------------------------
# OrderedDict: Remember the Order Keys Are Added to a Dictionary
# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

d = collections.OrderedDict()
for i in "abcdefghi":
    d[i] = i.upper()
print(d.keys())

# A regular dict looks at its contents when testing for equality. An OrderedDict also considers the 
# order in which the items were added.

d1 = collections.OrderedDict(a=1,b=2)
d2 = collections.OrderedDict(b=2,a=1)
print(d1==d2)

d.move_to_end("a")
print(d.keys())

# The collections.abc module contains abstract base classes that define the APIs for container data 
# structures built into Python and provided by the collections module. 

print([attr for attr in dir(collections.abc) if not attr.startswith("_")])