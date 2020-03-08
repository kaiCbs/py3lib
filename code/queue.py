# queue: Thread-Safe FIFO Implementation
# The queue module provides a first-in, first-out (FIFO) data structure suitable for 
# multithreaded programming. It can be used to pass messages or other data between 
# producer and consumer threads safely. Locking is handled for the caller, so many 
# threads can work with the same Queue instance safely and easily. The size of a Queue 
# (the number of elements it contains) may be restricted to throttle memory usage or 
# processing.

import queue


# ----------------------------------
# Basic FIFO Queue
# The Queue class implements a basic first-in, first-out container. Elements are added 
# to one “end” of the sequence using put(), and removed from the other end using get().
print("\nQueue")
q = queue.Queue()

for i in "Hello world Goodbye world".split():
    q.put(i)

while not q.empty():
    print(q.get() , end="! ")

# ----------------------------------
# LIFO Queue
# In contrast to the standard FIFO implementation of Queue, the LifoQueue uses last-in, 
# first-out ordering (normally associated with a stack data structure).
print("\nLIFO Queue")
q = queue.LifoQueue()

for i in "Hello world Goodbye world".split():
    q.put(i)

while not q.empty():
    print(q.get() , end="! ")


# ----------------------------------
# Priority Queue
# Sometimes the processing order of the items in a queue needs to be based on characteristics 
# of those items, rather than just the order they are created or added to the queue. 
print("\nPriority Queue")
fruits = ["apple","watermelon","banana","orange","mango"]

q = queue.PriorityQueue()

for i in fruits:
    q.put(i)

while not q.empty():
    print(q.get() , end=" ")


# ----------------------------------
# Building a Threaded Podcast Client
# TODO: finish after reading thread and urllib