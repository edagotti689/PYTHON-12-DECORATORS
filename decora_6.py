def p_decorate(func):
   def func_wrapper(name):
       if name == 'sriram':
           return " {0} Chowdary".format(func(name))
       else:
           return " Employee doesn't exist"
   return func_wrapper

@p_decorate
def get_text(name):
   return name

print(get_text('Kumar'))


