import re

text = "I am learning pythons regex"

result = re.search("python", text)

print(result)


#output will be something like this ---->

# <re.Match object; span=(14, 20), match='python'>