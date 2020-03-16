# heapq: Heap Sort Algorithm
# A heap is a tree-like data structure in which the child nodes have a sort-order relationship with the parents.
# Binary heaps can be represented using a list or array organized so that the children of element N are at
# positions 2*N+1 and 2*N+2 (for zero-based indexes). This layout makes it possible to rearrange heaps in place,
# so it is not necessary to reallocate as much memory when adding or removing items.

import math
from io import StringIO


# ----------------------------------
# Heap Output


def show(tree, total_width=36, fill=" "):
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write("\n")
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print("-" * total_width)
    print()


# ----------------------------------
# Creating a Heap
# There are two basic ways to create a heap: heappush() and heapify()

import heapq

data = [5, 54, 12, 4, 79, 31, 25, 10, 21, 1]
heap = []
print("random: ", data)

for n in data:
    print("add {:>3}:".format(n))
    heapq.heappush(heap, n)
    show(heap)

# If the data is already in memory, it is more efficient to use heapify() to rearrange the items of the
# list in place.

heapq.heapify(data)
print("heapified :", data)
show(data)

for i in range(5):
    smallest = heapq.heappop(data)
    print("pop {:>3}:".format(smallest))
    show(data)


# ----------------------------------
# Data Extremes from a Heap
# heapq also includes two functions to examine an iterable and find a range of the largest or smallest
# values it contains. Using nlargest() and nsmallest() is efficient only for relatively small values
# of n > 1, but can still come in handy in a few cases.

print("3 largest :", heapq.nlargest(3, data))


# ----------------------------------
# Efficiently Merging Sorted Sequences
# merge() uses a heap to generate a new sequence one item at a time, determining the next item using a fixed amount of memory.

data = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [-1, 3, 6, 10]]
print(list(heapq.merge(*data)))
