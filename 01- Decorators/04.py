import time
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func() 
        end_time = time.time()
        
        print(f'execution time for {func.__name__} = { end_time - start_time }')
    return wrapper

@calculate_execution_time
def myfunc():
    for x in range(10000000):
        pass
    
myfunc()