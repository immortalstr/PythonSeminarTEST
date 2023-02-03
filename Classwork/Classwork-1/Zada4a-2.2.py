# №2.2[11]. Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.
# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6

A = int(input())
if A == 0:
    print(1)
else:
    fib_prev, fib_next = 0, 1
    n = 2
    while fib_next <= A:
        if fib_next == A:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_next + fib_prev
        n+=1
    else:
        print(-1)

