# d = {}
# d = dict()

# d["q"] = "qwerty"
# print(d)
# d["w"] = 'warm'
# print(d)
# print(d["w"])
# d[865] = 865.234
# print(d)

# # for item in d:
# #     print(item,d[item])


# print(d.items())
# for (k, v) in d.items():
#     print(k, v)


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)
u = a.union(b)  # OБЪЕДИНЕНИЕ
i = a.intersection(b)  # ПЕРЕСЕЧЕНИЕ
d1 = a.difference(b)  # РАЗНОСТЬ a - b
q = a.union(b).difference(a.intersection(b))
print(q)