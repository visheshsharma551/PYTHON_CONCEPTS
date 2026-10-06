import re
result1 = re.search(r"\.", "Hello vishesh.")
print(result1.group())

result2 = re.search(r"\?","what are you doing?")
print(result2.group())


#r"\d" , \d is same as searching [0-9] (it finds one digit only), if want more add r"\d+"

result3 =re.search(r"\d","I am 35 years old")
print(result3.group())

result4 = re.search(r"\d+", "I am 35 years old")
print(result4.group())

result5 = re.search(r"\d{2,4}", "this is my phone number 41366")
print(result5.group())

result6 = re.search(r"\d{3}-\d{3}-\d{4}", "this is my phone number 562-732-9878")
print(result6.group())
