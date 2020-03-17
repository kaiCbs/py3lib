# calendar: Work with Dates
# The calendar module defines the Calendar class, which encapsulates
# calculations for values such as the dates of the weeks in a given month or
# year. In addition, the TextCalendar and HTMLCalendar classes can produce
# preformatted output.

import calendar


# ------------------------------------------------------------------------------
# Formatting Examples
# The prmonth() method is a simple function that produces the formatted text
# output for a month

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2020, 3)

# A similar HTML table can be produced with HTMLCalendar and formatmonth(). The
# rendered output looks roughly the same as the plain text version, but is
print(c.formatyear(2020, 2, 1, 6, 3))


# ------------------------------------------------------------------------------
# Locales
# To produce a calendar formatted for a locale other than the current default,
# use LocaleTextCalendar or LocaleHTMLCalendar.

c = calendar.LocaleTextCalendar(locale="en_US")
c.prmonth(2020, 3)

c = calendar.LocaleTextCalendar(locale="fr_FR")
c.prmonth(2020, 2)
