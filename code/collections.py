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

# TODO: defaultdict, deque, namedtuple, OrderedDict, collections.abc