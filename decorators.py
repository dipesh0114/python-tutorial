import time

def timer(func):
    def wrapper(*args, **kwargs):
         start = time.time()
         result = func(*args, **kwargs)
         end = time.time()
         print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
         return result
    return wrapper

@timer
def example_function(n):
     time.sleep(n)


example_function(2)
