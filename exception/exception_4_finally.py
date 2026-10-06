try:
    values = [1,2,3,4,5]
    result = values[int(input("Enter the index num here:  "))]
except IndexError:
    print("Index number doesn't exist")
else:
    print("result: ", result)    
finally:
    print("I will be printed all the time, regardless exception handled or not")        