# №2.1По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Примеры/Тесты:
# 5 -> Факториал 5 равен 120
# 0 -> Факториал 0 равен 1

'''N = int(input())
if N ==0:
    factorial=1
    print(factorial)
else:
    i = 1
    factorial = 1
    while i <= N:
        factorial *= i
        i += 1
    print(factorial)
'''
N = int(input())
if N == 0:
    factorial = 1
    print(factorial)
else:
    i = 1
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    print(factorial)
