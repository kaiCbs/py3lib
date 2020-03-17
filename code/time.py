# time: Clock Time
# The time module provides access to several types of clocks, each useful for
# different purpose. The standard system calls such as time() report the system
# "wall clock" time. The monotonic() clock can be used to measure elapsed time
# in a long-running process because it is guaranteed never to move backward,
# even if the system time is changed. For performance testing, perf_counter()
# provides access to the clock with the highest available resolution, which
# make short time measurements more accurate. The CPU time is available through
# clock(), and process_time() returns the combined processor and system time.

import time
import os


# ------------------------------------------------------------------------------
# Comparing Clocks

available_clocks = [
    ("clock", time.clock),  # has been deprecated in Python 3.3
    ("monotonic", time.monotonic),
    ("perf_counter", time.perf_counter),
    ("process_time", time.process_time),
    ("time", time.time),
]

for clock_name, func in available_clocks:
    print(
        """
        {name}:
        adjustable : {info.adjustable}
        implementation: {info.implementation}
        monotonic : {info.monotonic}
        resolution : {info.resolution}
        current : {current}
        """.format(
            name=clock_name,
            info=time.get_clock_info(clock_name),
            current=func(),
        )
    )


# ------------------------------------------------------------------------------
# Wall Clock Time
# time() returns the number of seconds since the start of the "epoch" as a
# floating-point value. The epoch is the start of measurement for time. Usually
# 0:00 on January 1, 1970. For logging or printting, ctime() will be better

print("The time is:", time.time())
print("The time is:", time.ctime())
print("The time after one minute is:", time.ctime(time.time() + 60))


# ------------------------------------------------------------------------------
# Monotonic Clocks
# Because time() looks at the system clock, and because the system clock can be
# changed by the user or system services for synchronizing clocks across
# multiple computers, calling time() repeatedly may produce values that go
# forward and backward. This can result in unexpected behavior when trying
# to measure durations or otherwise use those times for computation. To avoid
# those situations, use monotonic(), which always returns values go forward.

import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print("start : {:>9.2f}".format(start))
print("end   : {:>9.2f}".format(end))
print("span  : {:>9.2f}".format(end - start))


# ------------------------------------------------------------------------------
# Processor Clock Time
# Typically, the processor clock does not tick if a program is not doing
# anything. In this example, the loop does very little work by going to sleep
# after each iteration. The time() value increases even while the application
# is asleep, but the clock() value does not.

import time

template = "{} - {:0.2f} - {:0.2f}"
print(template.format(time.ctime(), time.time(), time.process_time()))
for i in range(3, 0, -1):
    print("Sleeping", i / 10)
    time.sleep(i / 10)
    print(template.format(time.ctime(), time.time(), time.process_time()))


# ------------------------------------------------------------------------------
# Performance Counter
# A high-resolution monotonic clock is essential for measuring performance.
# Determining the best clock data source requires platform-specific knowledge,
# which Python provides in perf_counter()


# ------------------------------------------------------------------------------
# Time Components
# The time module defines struct_time for holding date and time values, with
# the components being broken out so they are easy to access. Several functions
# work with struct_time values instead of floats.


def show(s):
    print("\n tm_year :", s.tm_year)
    print(" tm_mon :", s.tm_mon)
    print(" tm_mday :", s.tm_mday)
    print(" tm_hour :", s.tm_hour)
    print(" tm_min :", s.tm_min)
    print(" tm_sec :", s.tm_sec)
    print(" tm_wday :", s.tm_wday)
    print(" tm_yday :", s.tm_yday)
    print(" tm_isdst:", s.tm_isdst)


gmt = time.gmtime()
loc = time.localtime()
show(gmt)
show(loc)
print("\nmktime:", time.mktime(time.localtime()))

# The gmtime() function returns the current time in UTC. localtime() returns
# the current time with the current time zone applied. mktime() takes a
# struct_time and converts it to # the floating-point representation.

# ------------------------------------------------------------------------------
# Working with Time Zones
# To change the time zone, set the environment variable TZ, and then call
# tzset(). The following example changes the time zone to a few different
# values and shows how the changes affect other settings in the time module.


def show_zone_info():
    print(" TZ :", os.environ.get("TZ", "(not set)"))
    print(" tzname:", time.tzname)
    print(" Zone : {} ({})".format(time.timezone, (time.timezone / 3600)))
    print(" DST :", time.daylight)
    print(" Time :", time.ctime())
    print()


show_zone_info()

# ------------------------------------------------------------------------------
# Parsing and Formatting Times
# The functions strptime() and strftime() convert between struct_time and
# string representations of time values.

now = time.ctime(time.time())
parsed = time.strptime(now)
print("\nParsed:", parsed)
show(parsed)
print("\nFormatted:", time.strftime("%a %b %d %H:%M:%S %Y", parsed))

