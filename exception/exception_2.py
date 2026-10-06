# Create a program that:
# 
# Asks the user to enter a number.
# Converts it to an integer.
# Prints "Valid number" if successful.
# If the user enters something like "hello", prints "Invalid number".

try: 
    number = int(input("Enter your number :  "))
    print("valid number")
except ValueError:
    print("invalid number")
        
    
#value error and zero devision error 

try:
    num1= int(input("enter your 1st num:  "))
    num2 = int(input("enter your 2nd num:  "))
    
    result = num1/num2
    print(f"result:  {result}")
    
except ValueError:
    print("enter number")
except ZeroDivisionError:
    print("do not divide by zero")       
    
print("completed successfully")    

# Important thing to note here, if error occures and it is not handled in the exception, then python
#code stops there, won't go to the end to print ("completed successfully")