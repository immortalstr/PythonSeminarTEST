# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

numbers = [randint(-10,10) for i in range(randint(10,20))]
index_numbers = [i for i in range(len(numbers))]
print(*["{:3}".format(i) for i in numbers])
print(*["{:3}".format(i) for i in index_numbers])

minimum = int(input('Введите нижний диапазон: '))
maximum = int(input('Введите верхний диапазон: '))

min_max_numbers = [i for i in range(len(numbers)) if minimum <= numbers[i] <= maximum ]
print(min_max_numbers)
