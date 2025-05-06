l1 = [1,2,3]
l2 = l1
print(l1)
print(l2)

l1[0] = 44
print(l1)
print(l2)


p1 = [1,2,3]
p2 = p1
p2 = [1,2,3,]

p1[0] = 555
print(p1)
print(p2)

# copies using slicing methods 
p1 = [1,2,3]
p2 = p1[:]

p1[0] = 555
print(p1)
print(p2)
