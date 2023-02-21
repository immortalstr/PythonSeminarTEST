
# 5.2[28]: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 


def summ_of_numbers(a, b):
    if b == 0:
        return a
    else:
        return summ_of_numbers(a+1, b-1)

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))  
  
print(f'summ_of_numbers({x}, {y}) -> {summ_of_numbers(x, y)}')