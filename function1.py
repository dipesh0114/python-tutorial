import math

# def square(number):
#     return number **2

# result = square(4)    
# print(result)


# def sum_two(a,b):
#     return a+b

# a= int(input("enter a number: "))
# b= int(input("enter a number: "))

# result = sum_two(a,b)

# print(result)


def multiply(p1, p2):
    return p1 * p2

print(multiply(8,5))    
print(multiply('a',5))    
print(multiply(5,'a')) 

def circle_stats(radius):
    area = round((math.pi *radius **2),2)
    circumference = round((2 * math.pi * radius),2)
    return area, circumference


a,c = circle_stats(3)

print("area: ", a , ",circumference: ", c)

def greet (name = "user"):
    return "hello, " + name + " !"

print(greet("chai"))