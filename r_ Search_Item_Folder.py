"""
row
сравнивает название всех файлов в папке с названиями в текстовом файле и показывает каких файлов в папке не хватает.
"""
import os

sp_from_folder = os.listdir(input("Укажите путь к папке где лежат файлы (D:\\testPython\\photo): "))
# список из всех наименований файлов в папке
path_to_txt = input("Укажите путь к текстовому файлу (D:\\testPython\\spisok.txt): ")
znak = input('по какому знаку его разбить на список ( ): ')
key = input("Ключевое слово тех элементов, которые остануться в списке для сравнения (jpg): ")

with open(path_to_txt) as file:
    sp_from_file = file.read().split()

    print('----------------------------------------\nУдалённые элементы из списка: ')
    for stroka in sp_from_file:
        if key not in stroka:
            print(sp_from_file.pop(sp_from_file.index(stroka)), end=' ')
    print("\nИтого список: \n", sp_from_folder)
    print("\n----------------------------------------\nПропущенные файлы:\n")

for name in sp_from_file:
    if name not in sp_from_folder:
        print(name)

input("\nНажми любую кнопку для выхода")
