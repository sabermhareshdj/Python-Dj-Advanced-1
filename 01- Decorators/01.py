def mydecorator_function(func):
    def wrapper_fncation():
        print('Start ... ')
        func() 
        print('End .....')
    return wrapper_fncation



@mydecorator_function
def hello():
    print('Hello World .....')
    
hello()