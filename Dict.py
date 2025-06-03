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

