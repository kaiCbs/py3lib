# re: Regular Expressions
# Regular expressions are text matching patterns described with a formal syntax. The patterns are interpreted 
# as a set of instructions, which are then executed with a string as input to produce a matching subset or 
# modified version of the original. The term “regular expressions” is frequently shortened to “regex” or 
# “regexp” in conversation. Expressions can include literal text matching, repetition, pattern composition, 
# branching, and other sophisticated rules. A large number of parsing problems are easier to solve with a 
# regular expression than by creating a special-purpose lexer and parser.

import re


# ----------------------------------
# Finding Patterns in Text
# The search() function takes the pattern and text to scan, and returns a Match object when the pattern is 
# found. If the pattern is not found, search() returns None. The start() and end() methods give the indexes
#  into the string showing where the text matched by the pattern occurs.

pattern = "[0-9]+-[0-9]+"
text = "My phone number is 223-56413"

match = re.search(pattern, text)

s = match.start() 
e = match.end()

print("Found '{}'\nin '{}'\nfrom {} to {} ('{}')\n".format( match.re.pattern, match.string, s, e, text[s:e]))

# ----------------------------------
# Compiling Expressions
# Although re includes module-level functions for working with regular expressions as text strings, it is 
# more efficient to compile the expressions a program uses frequently. The compile() function converts an 
# expression string into a RegexObject.

regexes = [re.compile(p) for p in ["apple", "banana"]]
text = "Mike likes apple."

print('Text: {!r}\n'.format(text))

for regex in regexes:
    if regex.search(text):
        print("want a %s\n" % regex.pattern)
    else:
        print("No %s\n" % regex.pattern)

# ----------------------------------
# Multiple Matches
# search() to look for single instances of literal text strings. The findall() function returns all 
# of the substrings of the input that match the pattern without overlapping.

text = """We are transforming the event into Google Cloud Next ’20: Digital Connect, a free, 
global, digital-first, multi-day event connecting our attendees to Next ’20 content and each 
other through streamed keynotes, breakout sessions, interactive learning and digital “ask an 
expert” sessions with Google teams. Welcome to Google! """

pattern = "Google" 

for i, match in enumerate(re.findall(pattern, text)): 
    print("Found {!r} {} time".format(match, i+1) + "s" * (i>0))

# finditer() returns an iterator that produces Match instances instead of the strings returned by findall().
for match in re.finditer(pattern, text): 
    s, e = match.start(), match.end() 
    print("Found {!r} {} time".format(text[s:e], i+1) + "s" * (i>0), "at {:d}:{:d}".format(s, e))


# ----------------------------------
# Syntax

# TODO: to be finish


# ----------------------------------
# Escape Codes
# Escapes are indicated by prefixing the character with a backslash (\). Unfortunately, a backslash 
# must itself be escaped in normal Python strings, and that results in difficult-to-read expressions. 
# Using raw strings, which are created by prefixing the literal value with r, eliminates this 
# problem and maintains readability.

# TODO: to be finish


# ----------------------------------
# Anchoring
# In addition to describing the content of a pattern to match, the relative location can be specified 
# in the input text where the pattern should appear by using anchoring instructions.

# TODO: to be finish


# ----------------------------------
# Constraining the Search
# For example, if the pattern must appear at the front of the input, then using match() instead of search() 
# will anchor the search without having to explicitly include an anchor in the search pattern.

text = 'This is some text -- with punctuation.'
pattern = 'This'

m = re.match(pattern, text)  # yes
print('Match :', m) 
s = re.search(pattern, text) # yes
print('Search :', s)
f = re.fullmatch(pattern, text) # no
print('Full match :', f)


# ----------------------------------
# Dissecting Matches with Groups