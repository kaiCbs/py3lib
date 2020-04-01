# gc: Garbage Collector
# gc expose the underlying memory management mechanism of Python - automatic
# garbage collector. The module includes functions for controlling how the
# collector operates and examining the objects known to the system.

import gc
import queue
from pprint import pprint

# ------------------------------------------------------------------------------
# Tracing References
# With gc, the incoming and outgoing references between objects can be used to
# find cycles in complex data structures.
# get_referents() shows the objects referred  to by the input arguments


class Graph:
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)


p1 = Graph("p1")
p2 = Graph("p2")
p3 = Graph("p3")

p1.set_next(p2)
p2.set_next(p3)
p3.set_next(p1)

print("p3 refers to: ")
for r in gc.get_referents(p3):
    pprint(r)

seen = set()
to_process = queue.Queue()

to_process.put(([], p3))

while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print("Examining:", repr(next))
    seen.add(id(next))
    for r in gc.get_referents(next):
        if isinstance(r, str) or isinstance(r, type):
            pass
        elif id(r) in seen:
            print("\nFound a cycle to {}:".format(r))
            for i, link in enumerate(chain):
                print("   {}:".format(i), end="")
                pprint(link)
        else:
            to_process.put((chain, r))


# Forcing Garbage Collection
#
