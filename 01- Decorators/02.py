def mydecorator_function(func):
    def wrapper_fncation():
        result = func()
        return result.upper()
    return wrapper_fncation



@mydecorator_function
def hello():
    return 'Hello World .....'
    
print (hello())