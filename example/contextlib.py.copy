# contextlib: Context Manager Utilities
# The contextlib module contains utilities for working with context managers
# and the with statement

import contextlib
import io
import sys

# ------------------------------------------------------------------------------
# Context Manager API
# A context manager is responsible for a resource within a code block, possibly
# creating it when the block is entered and the cleaning it up after the block
# is exited.

with open("tempfile.txt", "wt") as f:
    f.write("This is a example.")

# A context manager is enabled by the with statement, and the API involves two
# methods. The __enter__() method is run when execution flow enters the code
# block inside the with statement. It returns an object to be used within the
# context. When execution flow leaves the with block, the __exit__() method of
# the context manager is called to clean up any resources that were used.
# Combining a context manager and the with statement is a more compact way of
# writing a try:finally block.


class Context:
    def __init__(self):
        print("__init__()")

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")


with Context():
    print("Working in the context")

# The __enter__() method can return any object to be associated with a name
# specified in the as clause of the with statement.


class WithinContext:
    def __init__(self, context):
        print("WithContext.__init__(%s)" % context)

    def do(self):
        print("Processing...")

    def __del__(self):
        print("WithinContext.__del__")


class Context:
    def __init__(self):
        print("__init__()")

    def __enter__(self):
        print("__enter__()")
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")


with Context() as c:
    c.do()

del c
# The __exit__() method receives arguments containing details of any exception
# raised in the with block.


class ContextError:
    def __init__(self, handle_err):
        print("__init__(%s)" % handle_err)
        self.handle_err = handle_err

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")
        print(" exc_type =", exc_type)
        print(" exc_val =", exc_val)
        print(" exc_tb =", exc_tb)
        return self.handle_err


print("Handle Error")

with ContextError(True):
    raise RuntimeError("error message handled")

# with ContextError(False):
#     raise RuntimeError("error message propagated")


# ------------------------------------------------------------------------------
# Context Managers as Function Decorators
# The class ContextDecorator adds support to regular context manager classes so
# that theycan be used as function decorators as well as context manegers.


class Context(contextlib.ContextDecorator):
    def __init__(self, how_used):
        self.how_used = how_used
        print("__init__({})".format(how_used))

    def __enter__(self):
        print("__enter__({})".format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__({})".format(self.how_used))


@Context("as decorator")
def func(message):
    print(message)


print()
with Context("as context manager"):
    print("Doing work in the contest")

print()
func("Doing work in the wrapped function")


# In those situations, the best approach is to use the contextmanager()
# decorator to convert a generator function into a context manager.


@contextlib.contextmanager
def make_context():
    print(" entering")
    try:
        yield {}
    except RuntimeError as err:
        print(" Error:", err)
    finally:
        print(" exiting")


print("Normal:")
with make_context() as f:
    print(" Inside:", f)

print("\nHandled error:")
with make_context() as value:
    raise RuntimeError("showing example of handling an error")

# print("\nUnhandled error:")
# with make_context() as value:
#     raise ValueError("this exception is not handled")


# The context manager returned by contextmanager() is derived from
# ContextDecorator, so itself also works as a function decorator.


@make_context()
def normal():
    print(" Inside")


@make_context()
def throw_error(err):
    raise err


print("Normal:")
normal()

print("\nHandled error:")
throw_error(RuntimeError("example of handling an error"))

# Note when the context manager is used as a decorator, the value yielded by
# the generator is not available inside the function being decorated.


# ------------------------------------------------------------------------------
# Closing Open Handles
# The file class supports the context manager API directly, but some other
# objects that represent open handles do not. The example given in the standard
# library documentation for contextlib is the object returned from
# urllib.urlopen(). Some other legacy classes use a close() method but do not
# support the context manager API.To ensure that a handle is closed, use
# closing() to create a context manager for it.


class Monitor:
    def __init__(self):
        print(" __init__()")
        self.status = "open"

    def close(self):
        print(" close()")
        self.status = "closed"


print("Normal:")
with contextlib.closing(Monitor()) as monitor:
    print(" Inside:%s" % monitor.status)
print(" Outside:%s" % monitor.status)


# ------------------------------------------------------------------------------
# Ignore Exceptions
# It is frequently useful to ignore exceptions raised by libraries, because the
# error indicates that the desired state has already been achieved or can
# otherwise be ignored. The most common way to ignore exceptions is with a
# try:except statement that includes only a pass statement in the except block.
# We can use contextlib.suppress() to replace try:expect that more explicitly
# suppress a class of exceptions happening anywhere the with block


class Trivial(Exception):
    pass


def operation():
    raise Trivial("a harmless error")


with contextlib.suppress(Trivial):
    print("Run operation")
    operation()
    print("Show if succeed")

print("done")


# ------------------------------------------------------------------------------
# Redirecting Output Streams
# Poorly designed library code may write directly to sys.stdout or sys.stderr,
# without providing arguments to configure different output destinations. The
# redirect_stdout() and redirect_stderr() context managers can be used to
# capture output from these kinds of functions.


def wrong_operation(a):
    sys.stdout.write(" stdout: %s\n" % a)
    sys.stderr.write(" stderr: %s\n" % a)


# print("Normal:")
# wrong_operation("Test")

print("\nRedirect:")

capture = io.StringIO()
with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
    wrong_operation("Test")

print(capture.getvalue())

# Both redirect_stdout() and redirect_stderr() modify the global state by
# replacing objects in the sys (page 1178) module; for this reason, they should
# be used with care. The functions are not really thread-safe, so calling them
# in a multithreaded application will have nondeterministic results. They also
# may interfere with other operations that expect the standard output streams
# to be attached to terminal devices.


# ------------------------------------------------------------------------------
# Dynamic Context Manager Stacks
# Most context managers operate on one object at a time, such as a single file
# or database handle. In these cases, the object is know in advance and the
# code using the context manager can be build around that one object. In other
# cases, a program may need to create an unknown number of objects within a
# context, with all of those objects expected to be cleaned up when control
# flow exits the context. ExitStack was created to handle these more dynamic
# cases. An ExitStack instance maintains a stack data structure of cleanup
# callbacks. The callbacks are populated explicitly within the context, and any
# registered callbacks are called in the reversed order when control flow exits
# the context.


@contextlib.contextmanager
def make_context(i):
    print("{} entering".format(i))
    yield {}
    print("{} exiting".format(i))


def var_stack(n, message):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(message)


var_stack(4, "Inside")

# enter_context() first calls __enter__() on the context manager. It then
# registers its __exit__() method as a callback to be invoked as the stack is
# undone.

# TODO: finish remaining part
