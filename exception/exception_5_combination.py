#if you have different exception but same message for all the exception , all exceptions can be combined


try:
    num1 = int(input("enter your first number here:  "))
    num2 = int(input("enter your second number here: "))
    result = num1/num2
except(ValueError, ZeroDivisionError, IndexError):
    print("something went wrong. Please try again")   
else:
    print("result: ", result)
finally:         
    print("i don't care, I will always be printed")