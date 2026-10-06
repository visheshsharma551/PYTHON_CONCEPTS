# ( ^ , $  and fullmatch())

import re
string = "Hello Vishesh, how are you doing?"   #( ^ finds the word/digit in the beginning of the string ,
#if we place digit/ word in the middle or last it won't find it)
result=re.search('^Hello',string)
print(result.group())



#. $ is used to find element at the end
# $ prevent extra text after the last match
string1 = "vishesh, Hello"
result1= re.search("Hello$",string1)
print(result1.group())

string2 ="helo234"
result2 = re.search("[0-9]$",string2)
print(result2.group())

string3 = "123456"
result3 = re.search("[0-9]{2,4}$", string3)
print(result3.group())


# using  ^ and $ together
# it finds the entire string from start to end 
result4 = re.search("^[0-9]{3}$", "123")
print(result4.group())
result5 = re.search("^[0-9]{5,8}$","676779")
print(result5.group())

result6 = re.search("^[a-z]+$","vishesh kumars harma")
# print(result6.group()) #nonetype

result7 = re.search("^[a-z]+$","visheshkumarsharma")
print(result7.group())




# fullmatch(), entire string must match the Pattern
#it is similar to "^[0-9]+$"

result8 = re.fullmatch("[0-9]+", "12349") #match
if(result8):
    print("it is full match")
else:
    print("it is not match")    
    
    
result9 = re.fullmatch("[a-z]+","visheshsharma")   #match
print(result9.group())   

result10 = re.fullmatch("[a-z]+","visheshsharma551")  #nomatch none is output
print(result10.group())   
