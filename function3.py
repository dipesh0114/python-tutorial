import math

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)


# resursive 

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5))    
