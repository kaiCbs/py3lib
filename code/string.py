# string: Text Constants and Templates

# The string module dates from the earliest versions of Python. Many of the functions previously
# implemented in the module have been moved to methods of str objects, but the
# module retains several useful constants and classes for working with str objects. This discussion
# will concentrate on them.

# ----------------------------------
# Functions 
print("\n $1 Functions\n")

import string
s = "This is a sentence without capitalizing words"
print(s)
print(string.capwords(s))

# ----------------------------------
print("\n $2 Templates\n")
# Templates
# String templates were added as part of PEP 2921 and are intended as an alternative to the
# built-in interpolation syntax. With string.Template interpolation, variables are identified
# by prefixing the name with $ (e.g., $var). Alternatively, if necessary to set them off from
# surrounding text, they can be wrapped with curly braces (e.g., ${var}).

values = {"var": "foo"}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('Template:', t.substitute(values))


s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print("INTERPOLATION:", s % values)


s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print("FORMAT:", s.format(**values))


# One key difference between templates and string interpolation or formatting is that the
# type of the arguments is not taken into account. The values are converted to strings, and
# the strings are inserted into the result. No formatting options are available. For example,
# there is no way to control the number of digits used to represent a floating-point value.

t = string.Template("$var is here but $missing is not provided")

print("safe_substitute():", t.safe_substitute(values))


# ----------------------------------
print("\n $3 Advanced Templates\n")
# Advanced Templates
# The default syntax for string.Template can be changed by adjusting the regular expression
# patterns it uses to find the variable names in the template body. A simple way to do that
# is to change the delimiter and idpattern class attributes.

class MyTemplate(string.Template):
    delimiter = "%"
    idpattern = "[a-z]+_[a-z]+" 


template_text = """
  Delimiter : %%
  Replaced  : %with_underscore
  Ignored   : %notunderscored
"""

d = {
    "with_underscore": "replaced",
    "notunderscored": "not replaced"
}

t = MyTemplate(template_text)

print("Modifed ID pattern:\n", t.safe_substitute(d))


# For even more complex changes, it is possible to override the pattern attribute and define
# an entirely new regular expression. The pattern provided must contain four named groups
# for capturing the escaped delimiter, the named variable, a braced version of the variable
# name, and invalid delimiter patterns.

print("Delimiter: ",string.Template('$var').delimiter)
print("Pattern: ",string.Template('$var').pattern.pattern)


# ----------------------------------
print("\n $3 Formatter\n")
# Formatter
# The Formatter class implements the same layout specification language as the format()
# method of str. Its features include type coersion, alignment, attribute and field references,
# named and positional template arguments, and type-specific formatting options. Most of the
# time the format() method is a more convenient interface to these features, but Formatter
# is provided as a way to build subclasses, for cases where variations are needed.

# TODO: add examples, https://docs.python.org/3.8/library/string.html#format-string-syntax


# ----------------------------------
print("\n $3 Constants\n")
# Constants

for 
