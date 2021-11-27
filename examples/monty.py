# Python basics

## Type hints
# type: ignore

## Importing
import re as regex
import matplotlib.pyplot as plt
from pprint import pprint
import importlib

## Muliline strings
s = """9noop9
afOo999
abar9001"""

## Regular expressions
# TODO: doesn't match last digit
my_regex = regex.compile("^[a-z](.*?)\d$", regex.I | regex.M)
pprint(my_regex.findall(s))

## Looping and iterators
for my_match in my_regex.finditer(s):
    print(my_match.group(1))

## Whitespace
# TODO: black should format matrices like a gentleman
eye = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

big_s = (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
)
