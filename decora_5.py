def p_decorate(func):
   def func_wrapper(n):
       return "{0} Chowdary".format(func(n))
   return func_wrapper

@p_decorate
def get_name(name):
   return name


df = get_name('sriram')

print(df)