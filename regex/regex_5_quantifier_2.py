#  (*), it means zero occurrence or more 
import re
input_5 = "fjksaaaaaacd13e232"
result = re.search("a*cd", input_5)
#  a* means zero or more a
print(result.group())


# (?) optional quantifier

input_1  = "I have 2 woksheet"
result_2 = re.search("wor?ksheets?", input_1) #it will skip the letters which are optional
print(result_2.group())

# {} exact quantifiers, searches the letter/digit  for the positions
# exact mentioned numbers of times eg. [0-9]{4} , [a-z]{3}

input_2 = "423213213321"
result_3 = re.search("[0-9]{5}",input_2)
print(result_3.group())

#{2,5} it can also search for between 2 and 5 but not 1 

input_3 = "abckyj34234434"
result_4 = re.search("[0-9]{2,5}",input_3)
print(input_3 + ": " +result_4.group())


