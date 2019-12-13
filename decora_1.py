'''
Python supports the concept of First Class functions.

Properties of first class functions:
    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists, …

'''

def Hello_word(name):
    print(' Name is :', name)

k = Hello_word
k('Dinesh')