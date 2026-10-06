# try:
#     riskOperation()
# except:
#     handleOperation()
# else:
#     successOperation()    

# try:
#     num1 = int(input("enter your 1st number:  "))
#     num2 = int(input("enter your 2ne number:  "))
#     result = num1/num2
    
# except ValueError:
#     print("please enter number")
# except ZeroDivisionError:
#     print("number can not be divided by zero.please enter positive number") 
# else:
#     print("result: ", result)
#     print("result printed successfully")       
    
    
    
try:
    randomList= ["helllo", "vishesh", 5, 7, "danielle"]
    randomListIndex = randomList[int(input("enter your index number: "))]
except IndexError:
    print("entered index number doesn't exist")
except ValueError:
    print("index number doesn't exist in string, enter number")
else:
    print("successfull result:  ",randomListIndex)   
    
        
        
        