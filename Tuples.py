tea_types = ("black", "green", " oolong")

more_tea = ("herbal", "earl grey")
all_tea = more_tea + tea_types
print(all_tea)

if "green " in all_tea:
    print("i have a green tea")

(black, green, oolong) = tea_types
print(black)    
print(type(tea_types))

