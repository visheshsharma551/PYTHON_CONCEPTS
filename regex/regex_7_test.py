import re

text = "123abc"

result = re.search("[0-9]+", text)

print(result.group())