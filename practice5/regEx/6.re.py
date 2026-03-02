#re.findall
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
#re.search
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#re.split
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#re.sub
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#re.match
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())