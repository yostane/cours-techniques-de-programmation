numbers = [3, 49, 2, -29, 17]
numbers.append(1000)

print(len(numbers))

print(numbers[2:4])
print(numbers[2:])
print(numbers[:3])

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

for i in [10, 12, 14]:
    print(i)

for i in range(10, 100001, 1000):
    print(i)

print("done")

# les Tuples n'acceptent pas d'ajout ou de suppression d'éléments ni changer d'élements
t1 = (1, 3, 10, 555)
print(t1)
