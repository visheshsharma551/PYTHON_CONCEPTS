# (+, *, ?, {})
# character class tells Regex "what kind of character to look for"
# quantifier tells Regex "how many times that thing appeared"
import re

phoneNum = "5627329878"

result = re.search("[0-9]+", phoneNum)


print(result.group())


# As long as digits are next to each other , it searches and find the first section of digits

introduction = "I am 34 years old and my brother was 4 year older than me."

output = re.search('[0-9]+', introduction)

print(output.group())



#[0-9]+  will search only for digits in the string, not whole string

string = "1234abcd"

result_1 = re.search("[0-9]+",string)

print (result_1.group())

#[a-z]+. same goes for  letters , it searches for letters in the string

result_2 = re.search("[a-z]+", string)
print(result_2.group())
 