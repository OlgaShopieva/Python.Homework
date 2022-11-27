# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input('Введите число: ')
# summa = 0
# for i in num:
#     if i.isdigit():
#         summa += int(i)

# print(summa)


# #Задача 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def Factorial(n):
#     list = []
#     count = 1
#     for i in range (1, n + 1):
#         count *= i
#         list.append((count))
#     return list
    
# n = int(input('Введите число: '))
# list2 = Factorial(n)
# print(list2)


# #Задача 3: Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# some_dict = {}
# n = int(input('Введите число: '))
# sum = 0
# for i in range(1, n + 1):
#     some_dict[i] = (1 + (1 / i)) ** i
# for k, v in some_dict.items():
#     print(f'{k}: {round(v, 2)}', end=', ')
#     sum += v
# print()
# print(f'Сумма чисел в списке: {round(sum, 2)}')


#Задача 4: Реализуйте алгоритм перемешивания списка.
# import random
# list = ["ab", "bc", "cd", "de", "ef"]
# random.shuffle(list)
# print(list)








