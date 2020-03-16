# ------------------------------------------------------------------------------
# Example one: record when the function was initiated

import datetime


def time_recorder(func):
    init_time = datetime.datetime.now()

    def wrapped(*args, **kwargs):
        print(func.__name__, "initiated at:", init_time)
        return func(*args, **kwargs)

    return wrapped


# The normal way ×
abs_new = time_recorder(abs)
print(abs_new(-12))

sum_new = time_recorder(sum)
print(sum_new(range(10)))


# The Pythonic way √
@time_recorder
def pow_new(x, n):
    return x ** n


print(pow(2, 7))
