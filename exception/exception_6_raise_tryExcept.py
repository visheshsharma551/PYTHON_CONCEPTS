try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age")

except ValueError as e:
    print("this is the error: " ,e)