import time
import math
import inspect


def timeit(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time Usage: %.3fs" % (end - start))
        return result

    return timed


@timeit
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


for i in range(1, 4):
    print("There are %d primes within %d" % (len((primes(10 ** i))), 10 ** i))


# The syntax for decorators with arguments is a bit different - the decorator
# with arguments should return a function that will take a function and return
# another function. So it should really return a normal decorator.


def repeating(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for i in range(repeat):
                print(
                    "The answer of %s is"
                    % (func.__name__ + str(inspect.signature(func))),
                    result,
                )
            return result

        return wrapper

    return decorator


@repeating(5)
def pow(x, n):
    return x ** n


pow(4, 4)
