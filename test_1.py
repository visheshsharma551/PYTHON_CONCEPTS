def main_function(function):
    def wrapper(x):
        return function(x).upper()
    
    return wrapper

@main_function
def my_name(name):
    return f"I am {name}"

print(my_name("vishesh kumar sharma"))