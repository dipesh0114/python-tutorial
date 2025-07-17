import time

def cache(func):
    cache_value = {}
    print("Cache initialized")
    def wrapper(*args):  
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result  
        return result
    return wrapper

@cache
def long_running_function(a, b):    
    time.sleep(4)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(2, 3))  # This will return the cached result without delay
print(long_running_function(3, 4))  # This will take time as it's a new call