import re

txt = "Hello World"
x = re.search("hello", txt, re.IGNORECASE)

if x:
    print("Match found!")
else:
    print("No match")

import re

txt = """Hello
World
Python"""

x = re.search("^World", txt, re.MULTILINE)

if x:
    print("Found at start of a line!")
else:
    print("No match")

import re

txt = "Hello\nWorld"

x = re.search("Hello.*World", txt, re.DOTALL)

if x:
    print("Match across lines!")
else:
    print("No match")

import re

pattern = r"""
\d{3}   # three digits
-       # dash
\d{2}   # two digits
"""

x = re.search(pattern, "123-45", re.VERBOSE)

if x:
    print("Matched!")

re.search("hello", txt, re.IGNORECASE | re.MULTILINE)