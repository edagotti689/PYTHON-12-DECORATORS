'''
In python we can pass function as argument to the another fucntion and we can call that function inside function.

'''
def Hello_word(f):
    f(2, 5)

def add(a,b):
    print(' \n sum is :', a + b)

Hello_word(add)

