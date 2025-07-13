age = int(input("enter your age : "))
day = input("enter day : ")

price = 12 if age >=18 else 8

if (day == "wednesday" or day== "wed"):
    price -= 2

print("your ticket price is $", price)