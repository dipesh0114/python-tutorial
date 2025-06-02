tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])

tea_varities[3] = "herbal"
print(tea_varities)

# tea_varities[1:2] = ["lemon"]
tea_varities[1:3] = ["lemon", "masala"]
print(tea_varities)

tea_varities[1:1] = ["test", "test"]
print(tea_varities)

tea_varities[1:3] = []
print(tea_varities)

for tea in tea_varities:
    print(tea, end="-")

if "oolong" in tea_varities:
    print("I have oolong tea")

tea_varities.append("oolong")    

tea_varities.insert(1, "green")
tea_varities_copy = tea_varities.copy()

squared_num = [x**2 for x in range(10)]
print(squared_num)

