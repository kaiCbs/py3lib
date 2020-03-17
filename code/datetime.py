# datetime: Date and Time Value Manipulation
# datetime contains functions and classes for date and time parsing, formatting,
# and time parsing, formatting, and arithmetic.

import datetime
import time

# ------------------------------------------------------------------------------
# Times
# Time values are represented with time class. A time instance has atttribute
# for hour, minute, second, and microsecond; it can also include time zone
# information.

print("Earliest :", datetime.time.min)
print("Latest :", datetime.time.max)
print("Resolution:", datetime.time.resolution)


t = datetime.time(1, 2, 3)
print(t)
print("hour        :", t.hour)
print("minute      :", t.minute)
print("second      :", t.second)
print("microsecond :", t.microsecond)
print("tzinfo      :", t.tzinfo)
print("Earliest :", datetime.time.min)
print("Latest :", datetime.time.max)
print("Resolution:", datetime.time.resolution)

import datetime

for m in [0, 1, 10, 600]:
    print("{:02.1f} :".format(m), datetime.time(0, 0, 0, microsecond=m))

# ------------------------------------------------------------------------------
# Calender date values are represented with the date class. Instance have
# attributes for year, month, and day. It is easy to create a date representing
# the current date using the today() class method

today = datetime.date.today()
print(today)
print("time c:", today.ctime())

timetuple = today.timetuple()
attrs = [m for m in dir(timetuple) if m.startswith("tm")]
for m in attrs:
    print("%10s =" % m, getattr(timetuple, m))
print("ordinal:", today.toordinal())
print("Year :", today.year)
print("Mon :", today.month)
print("Day :", today.day)

o = 737501
print("o :", o)
print("fromordinal(o) :", datetime.date.fromordinal(o))
t = time.time()
print("t :", t)
print("fromtimestamp(t):", datetime.date.fromtimestamp(t))


print("Earliest :", datetime.date.min)
print("Latest :", datetime.date.max)
print("Resolution:", datetime.date.resolution)

# Another way to create new date instances is to use the replace() method of an
# existing date.
d1 = datetime.date(2008, 3, 29)
print("d1:", d1.ctime())
d2 = d1.replace(year=2009)
print("d2:", d2.ctime())


# ------------------------------------------------------------------------------
# timedeltas
# Future and past dates can be calculated using basic arithmetic on two
# datetime objects, or by combining a datetime with a timedelta. Subtracting
# dates produces a timedelta, and a timedelta can be also added or subtracted
# from a date to produce another date.

print("microseconds:", datetime.timedelta(microseconds=1))
print("milliseconds:", datetime.timedelta(milliseconds=1))
print("seconds :", datetime.timedelta(seconds=1))
print("minutes :", datetime.timedelta(minutes=1))
print("hours :", datetime.timedelta(hours=1))
print("days :", datetime.timedelta(days=1))
print("weeks :", datetime.timedelta(weeks=1))

# we can use total_second() to convert in to seconds

print(datetime.timedelta(weeks=1).total_seconds())


# ------------------------------------------------------------------------------
# Date Arithmetic
# Date math uses the standard arithmetic operators.

today = datetime.date.today()
print("Today :", today)
one_day = datetime.timedelta(days=1)
print("One day :", one_day)
yesterday = today - one_day
print("Yesterday:", yesterday)
tomorrow = today + one_day
print("Tomorrow :", tomorrow)

print("1 day :", one_day)
print("5 days :", one_day * 5)
print("1.5 days :", one_day * 1.5)
print("1/4 day :", one_day / 4)
# Assume an hour for lunch.
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print("meetings per day :", work_day / meeting_length)


# ------------------------------------------------------------------------------
# Comparing Values
# Both date and time values can be compared using the standard comparision
# operators to determine which is earlier or later.

print("Dates:")
d1 = datetime.date.today()
print(" d1:", d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print(" d2:", d2)
print(" d1 > d2:", d1 > d2)


# ------------------------------------------------------------------------------
# Combining Dates and Times
# Using the datetime class to hold values consisting of both date and time
# components. As with date, several convenient class methods are available for
# creating datetime instances from other common values.

now = datetime.datetime.now()
print(now.year, now.month, now.day)

# ------------------------------------------------------------------------------
# Formatting and Parsing
# The default string representation of a datetime object uses the
# ISO-8601 format (YYYY-MMDDTHH:MM:SS.mmmmmm).
# Alternative formats can be generated using strftime().

format = "%a %b %d %H:%M:%S %Y"
print(now)
print(now.strftime(format))

# Use datetime.strptime() to convert formatted strings to datetime instances.

formatted = now.strftime(format)
datetime.datetime.strptime(formatted, format)

# check strptime/strftime format codes at https://strftime.org/


# ------------------------------------------------------------------------------
# Time Zones
# Within datetime, time zones are represented by subclasses of tzinfo. Since
# tzinfo is an abstract base class, applications need to define a subclass and
# provide appropriate implementations for a few methods to make it useful.

min6 = datetime.timezone(datetime.timedelta(hours=-6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d = datetime.datetime.now(min6)
print(min6, ":", d)
print(datetime.timezone.utc, ":", d.astimezone(datetime.timezone.utc))
print(plus6, ":", d.astimezone(plus6))
# Convert to the current system timezone.
d_system = d.astimezone()
print(d_system.tzinfo, " :", d_system)

# The third-party module pytz is a better implementation for time zones. It
# supports named time zones, and the offset database is kept up-to-date as
# changes are made by political bodies around the world.
