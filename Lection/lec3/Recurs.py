def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

lsit_1 = []
for i in range(1,10):
    lsit_1.append(fib(i))
print(lsit_1)