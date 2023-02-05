# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# # colors.remove('red')
# colors.discard('red')
# print(colors)

# colors.clear()
# print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)
u = a.union(b)  # OБЪЕДИНЕНИЕ
i = a.intersection(b)  # ПЕРЕСЕЧЕНИЕ
d1 = a.difference(b)  # РАЗНОСТЬ a - b
q = a.union(b).difference(a.intersection(b))
print(q)

# ЗАМОРОЖЕННОЕ МНОЖЕСТВО

a = {1,8,6}
b = frozenset(a)

print(b)