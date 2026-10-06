import re

introduction = "I am visheh kumar sharma"
result =re.search("sharma",introduction )

print(result.group())       #it returns exact match , no pattern type output


print(f"what is vishesh kumar's last name? : {result.group().upper()}")