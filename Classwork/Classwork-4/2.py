# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# new_text = text.lower()

# print(len(set(text.split())))
# print(len(set(new_text.split())))

# text = """She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells."""

# text = text.split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# n = int(input())
# max_number = n # - Должно быть n
# while n != 0:
#     n = int(input())
#     if max_number < n: # n > max_number
#         max_number = n  
# print(max_number)

# Петя:
n = int(input()) # 45
max_number = -1 
while n != 0: # - неправильный выход
      # 4 
    if max_number < n: 
        max_number = n # - ошибка max_number = n
    n = int(input())
print(max_number) # - ошбиика