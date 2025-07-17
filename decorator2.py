def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling function '{func.__name__}' with arguments: {args_value} and keyword arguments: {kwargs_value}")
        result = func (*args, **kwargs)
        return result
    return wrapper


@debug
def hello():
    print("Hello, world!")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

hello()
greet("chai", greeting="Hanji")        