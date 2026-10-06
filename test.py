def greetings(message):
    return f"hello {message}"

def change_case(function):
    def wrapper(x):
       return function(x).upper()
    return wrapper
    
result1 = change_case(greetings)

print(result1("welcome"))   


@change_case
def my_self(name):
    return f"{greetings('welcome')} I am {name}" 

print(my_self("vishesh kumar sharma"))