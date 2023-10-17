def decorator_with_arguments(arg1,arg2):
       
    def mydecorator_function(func):
        def wrapper(*args, **kwargs):
            print (f'arg1 : {arg1} - Arg2: {arg2}')
            
            if arg1 < 0 or arg2 < 0 :
                return 'x & y must be > = 0'
            else:
                func(*args, **kwargs)
                
        return wrapper
    return mydecorator_function



@decorator_with_arguments(3,5)
def mysum(x,y):
    return x+y
    
print (mysum(3,5))