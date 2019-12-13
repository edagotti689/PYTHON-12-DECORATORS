def get_name():
   return 'SRIRAM'

def p_decorate(f):
   def func_wrapper():
       return "{0} Chowdary".format(f())
   return func_wrapper


wf = p_decorate(get_name)

r = wf()
print(r)