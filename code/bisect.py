# bisect: Maintain Lists in Sorted Order
# The bisect module implements an algorithm for inserting elements into a list while 
# maintaining the list in sorted order.

import bisect


# ----------------------------------
# Inserting in Sorted Order
# insort() is used to insert items into a list in sorted order
# bisect() return the index where to insert item x in list a
values = [3,51,4,79,12,4,4,38,51,100]

l = [] 
for i in values: 
    position = bisect.bisect(l, i) 
    bisect.insort(l, i) 
    last = l[:]
    last[position] = "V"
    print('Insert {:3} at{:3}  '.format(i, position),last)
    print(">> "," "*14, l)


# ----------------------------------
# 2.5.2 Handling Duplicates
# The bisect module provides two ways to handle repeats: New values can be inserted 
# either to the left of existing values, or to the right. The insort() function is 
# actually an alias for insort_right(), which inserts an item after the existing value. 
# The corresponding function insort_left() inserts an item before the existing value.
# The bisect module provides two ways to handle repeats: New values can be inserted 
# either to the left of existing values, or to the right. The insort() function is 
# actually an alias for insort_right(), which inserts an item after the existing value. 
# The corresponding function insort_left() inserts an item before the existing value.

l = [] 
for i in values: 
    position = bisect.bisect_left(l, i) 
    bisect.insort_left(l, i) 
    last = l[:]
    last[position] = "V"
    print('Insert {:3} at{:3}  '.format(i, position),last)
    print(">> "," "*14, l)