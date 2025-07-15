cube = lambda x: x**3

print(cube(5))

def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum (args)

print(sum_all(1,2,3))    
# print(sum_all(1,2,3,4,5))    
# print(sum_all(1,2,3,4,5,6,7,8))    

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "ironman", power = "suit")        
print_kwargs(name = "ironman")        
print_kwargs(name = "ironman", power = "suit", enemy= "Thanos")       


