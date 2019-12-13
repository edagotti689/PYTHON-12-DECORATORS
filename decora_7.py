'''
1. Using decorators we can change a behaviour of function without changing any fucntion code.
2. using @ we can assign decorator to the function

## How to create decorator
Decorator fucntion takes one argument as function
Decorator function contains another wrapper function
Inside wrapper function only we have to call function argument
Decorator function will return wrapper function
'''

def dec_fun(f):
    def wrap_fun():
        return float(f())
    return wrap_fun

@dec_fun
def add():
    return 2 + 3

print(add())