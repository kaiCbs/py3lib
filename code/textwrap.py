import textwrap

# textwrap: Formatting Text Paragraphs
# The textwrap module can be used to format text for output in situations where prettyprinting
# is desired. It offers programmatic functionality similar to the paragraph wrapping
# or filling features found in many text editors and word processors.

sample_text = """
    The textwrap module can be used to format text for output in situations where prettyprinting
    is desired. It offers programmatic functionality similar to the paragraph wrapping or filling
    features found in many text editors and word processors.
"""


# ----------------------------------
# Filling Paragraphs

print(sample_text)
print(textwrap.fill(sample_text, width=50))


# ----------------------------------
# Removing Existing Indentation
# Removing the common whitespace prefix from all of the lines in the sample text with dedent() 
# produces better results and allows the use of docstrings or embedded multiline strings straight 
# from Python code while removing the formatting of the code itself. 

denteded = textwrap.dedent(sample_text)
print(denteded)


# ----------------------------------
# Indenting Blocks

print(textwrap.indent(denteded, ">> "))


# ----------------------------------
# Truncating Long Text

print(textwrap.shorten(sample_text, 100))