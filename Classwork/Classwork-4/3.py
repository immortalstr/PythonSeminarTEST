n = 6
# lst1 = [0] * (n + 1)
lst1 = [0 for i in range(n+1)]
for i in range(n+1):
    lst1[i] = 3*i + 1

print(lst1)

print([(3*i + 1) for i in range(n+1)])


lst1 = [0] * (3*n + 2)
for i in range(n+1):
    lst1[3*i + 1] = 3*i + 1
print(lst1)