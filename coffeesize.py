order_size = input("enter your coffee size (small or medium or large) : ")
extra_shot = False

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee" 

print("order: ",coffee)       