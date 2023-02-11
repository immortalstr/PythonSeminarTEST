# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def pow_of_numbers(a, b):
    if b == 1:
        return a
    else:
        return pow_of_numbers(a, b-1) * a

x = int(input("Введите число которое возводится в степень: "))
y = int(input("Введите число степени этого числа: "))   

print(f'pow_of_numbers({x}, {y}) -> {pow_of_numbers(x, y)}')