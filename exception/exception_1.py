#Python runs your code, reaches problematic line of code and raises exception : runtime Error

# try this code, if something goes wrong , handle the problem instead of crashing 
#i.e  try and except 
# num_1 = int(input("enter your num"))
# num_2 = int(input("enter your num"))
# result = num_1/num_2
# print("result: ",result) # here could be possible scenarios that code could fail 
#                          # user enters string instead of number 
#                          #user divides num_1 with 0
                         
# numbers = [1,2,3,4]
# print(numbers[6])     #index doesn't exist

# object = {"name":"vishesh"}
# # print(object["age"])                    #key doesn't exist in dictionary


#try and exception 

try:
    number = int(input("enter your number here :  "))
    print(f"you entered: {number}")
except:
    print("you entered string not number, something went wrong, please try again.")    
    
