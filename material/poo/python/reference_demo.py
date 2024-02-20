x = 10
# Copie de la valeur
y = x
y = 11
print(x, y)

items = [1, 2, 3, 4]
# Copie de la référence
other_items = items

items[-1] = 100
print(items, other_items)

test2_items = [1, 2, 3, 4]
other_test2_items = test2_items[:]
# copie avec un boucle for
other_clone_items2 = []
for item in test2_items:
    other_clone_items2.append(item)

test2_items[-1] = 100
other_test2_items[2] = -66
print(test2_items, other_test2_items, other_clone_items2)
