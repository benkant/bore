# Type hints
# type: ignore

# Importing
import re as regex
import matplotlib.pyplot as plt

# Muliline strings
s = """9noop9
afoo999
abar9001"""

# Regular expressions
my_regex = regex.compile("^[a-z](.*?)\d(3,)$", regex.I | regex.M)

# Looping and iterators
for my_match in my_regex.finditer(s):
    print(my_match.group(1))

    
