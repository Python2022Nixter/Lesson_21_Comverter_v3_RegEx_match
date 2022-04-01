# Regular Expressions, Regex, Regexp, Regular Expression

# https://regex101.com/

from ast import pattern
import re

test_string = "My test text string ."
pattern = r"\st"
"""
    findall -> returns a list of all matches
    search -> returns the first match
    split -> returns a list of all matches
    sub -> returns a string with all matches replaced
"""

res = re.search(pattern, test_string)
print(res)
res = re.split("\s", test_string)
print(res)
res = re.sub("\s", "_", test_string)
print(res)