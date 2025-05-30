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

