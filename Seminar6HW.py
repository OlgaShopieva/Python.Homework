# Задача1:Напишите функцию, которая переворачивает строку

# def reverse(input_str):
#
#     out_str=''
#     for i in range(len(input_str)-1,-1,-1):
#         out_str += input_str[i]
#     return out_str
# some_str = input('Введите строку: ')
# print(reverse(some_str))

# Задача2: Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2] Надо вернуть их пересечение [1, 2, 2, 3](порядок неважен)

# a = [1, 2, 3, 2, 0]
# b = [5, 1, 2, 7, 3, 2]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)


# Задача6:
# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений
# input_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
# ind = 0
# count = 1
# out_str = ""
# while ind < len(input_str) - 1:
#     if input_str[ind] == input_str[ind + 1]:
#         count += 1
#     else:
#         if count == 1:
#             out_str += input_str[ind]
#         else:
#             out_str += input_str[ind] + (str(count))
#         count = 1
#     ind += 1
#
# print(out_str)






