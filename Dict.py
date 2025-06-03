chai_types = {"masala":"spicy", "Ginger": "Zesty", "Green":"Mild"}

y = chai_types["masala"]
x = chai_types.get("masala")
z = chai_types.get("msasaals")

print(x)
print(y)
print(z)

for chai in chai_types:
    print(chai, chai_types[chai])


for key, value in chai_types.items():
    print(key, value)

chai_types["earl grey"] = "Citrus"
print(chai_types)   

tea_shop = {
    "chai" : {"masala":"spicy", "ginger": "zesty"},
    "Tea": {"green":"mild", "black" :"strong"}
}

print(tea_shop['chai'])
print(tea_shop['chai']['ginger'])

squared_num = {x:x**2 for x in range(6)}
print(squared_num)

keys = ["msala", "ginger", "lemon"]
default_value = "delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

