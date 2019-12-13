'''
In python we can create a function inside another function and we can call inside same fucntion.

If you want to call outside a fnction we have to return that function

'''

def Hello_word(name):
    print(" Name is : " , name)

    def add():
        print( '\n Add is :',  2 + 2)

    return add

f = Hello_word('nagesh')
f()