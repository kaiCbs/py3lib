# weakref: Impermanent References to Objects
# The weakref module supports weak references to objects. A normal reference increments the
# reference count on the object and prevents it from being garbage collected. This outcome is
# not always desirable, especially when a circular reference might be present or when a cache
# of objects should be deleted when memory is needed. A weak reference is a handle to an
# object that does not keep it from being cleaned up automatically.

import weakref

# ----------------------------------
# References
# Weak references to objects are managed through the ref class. To retrieve the original object,
# call the reference object.

class ExpensiveObj:

    def __del__(self):
        print("Deleting {} ...".format(self))

obj = ExpensiveObj()    
r = weakref.ref(obj)
print('obj:', obj)
print('ref:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())

# In this case, since `obj` is deleted before the second call to the reference, the `ref` returns None.        

# ----------------------------------
# Reference Callbacks
# The `ref` constructor accepts an optional callback function that is invoked when the referenced object 
# is deleted. The callback receives the reference object as an argument after the reference is “dead” and 
# no longer refers to the original object. One use for this feature is to remove the weak reference 
# object from a cache.

def callback(reference):
    print("callback({!r})".format(reference))

obj = ExpensiveObj()
r = weakref.ref(obj, callback)

print("obj:", obj)
print("ref:", r)
print("r()", r())
print('deleting obj')
del obj
print("r():", r())


# ----------------------------------
# Finalizing Objects
# For more robust management of resources when weak references are cleaned up, use finalize() to 
# associate callbacks with objects. A finalize instance is retained until the attached object is 
# deleted, even if the application does not retain a reference to the finalizer.

def on_finalize(*args):
    print('\non_finalize({!r})'.format(args[0])*args[1])

obj = ExpensiveObj()
weakref.finalize(obj, on_finalize, 'extra argument', 3)

del obj