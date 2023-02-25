# Задача 38. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import csv



phonebook = {}

# def get_data(pb):
#     surname = input("Введите Фамилию: ")
#     name = input("Введите Имя: ")
#     patronymic = input("Введите Отчество: ")
#     phone_number = input("Введите номер телефона: ")
#     return (surname, name, patronymic,phone_number)

# def id_client(data:tuple):
#     id = data[3]
#     return id

# def create_new_contact(pb,data,id):
#     pb[id] = data
#     return pb


# create_new_contact(phonebook,get_data(phonebook),id_client(get_data(phonebook)))

print(phonebook)

# phonebook[1] = ("asd")
# print(phonebook)
phonebook[2] = ("asasdd")
print(phonebook)

# def add_in_file(pb,file_name):

#     with open(file_name, 'w') as file:
#         for (i,k) in pb.items():
#             file.write(i,k)

# file_name = 'data.txt'

# get_data(phonebook)



# print(phonebook)
