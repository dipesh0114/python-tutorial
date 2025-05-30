chai = "lemon chai";
print(chai)


first_char = chai[0]

print(first_char)

chai1 = "masala chai"
slice_chai = chai1[0:6]
slice_chai1 = chai1[:]
slice_chai2 = chai1[5:]

print(slice_chai)
print(slice_chai1)
print(slice_chai2)

num_list = "11124567889"

slice_num = num_list[0:7:2]
print(slice_num)

print(chai.lower())
print(chai.upper())

print(chai.replace('lemon','ginger'))

chai2 = "lemon, giner, masala, mint"
print(chai2.split())
print(chai2.split(", "))

print(chai.find("chai"))
print(chai.find("Chai"))

chai_type = "Masala"
quantity = 2 
order = "I ordered {} cups of {} chai"

print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))

print(len(chai))

# for letter in chai:
#     print(letter)

chai4 = "masala\nchai"
print(chai4)

chai5 = r"Masala\nchai"
print(chai5)

url = r"c:\user\pwd"
print(url)

print("c:\\user\\pwd")

