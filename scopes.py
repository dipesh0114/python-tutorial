username = "chaiaaurcode"

def func():
    username = "chai"
    print(username)

print(username)
func()    

x= 99 
def func2(y):
    z = x + y
    return z

result = func2(10)
print(result)  # Output: 109

# climbing

def f1():
    x= 88
    def f2():
        print(x)
    f2()
f1()  # Output: 88  

# closure

def chaicoder(num):
    def inner_func(x):
        return x ** num
    return inner_func

squared = chaicoder(2)  # this saves in different memory location
cubed = chaicoder(3)     # this saves in different memory location

print(squared)  #<function chaicoder.<locals>.inner_func at 0x000001AD52BF9300>
print(cubed)    #<function chaicoder.<locals>.inner_func at 0x000001AD52BF93A0>

print(squared(5))  # Output: 25
print(cubed(5))    # Output: 125

