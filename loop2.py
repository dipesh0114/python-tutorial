n = int(input("enter a number: "))
sum_even = 0

for i in range (1, n+1):
    if i%2 == 0:
        sum_even += i

print("the sum of even numbers = ", sum_even)        