# Задача38: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# txt = 'абв гн южэ нар дав прн wytr'
# txt_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, txt.split()))
# print(txt_list)

# Задача40: Создайте программу для игры в крестики-нолики
# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


# Задача41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def compress(file, compressedfile):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(compressedfile, 'w', encoding='utf-8') as res:
#             input_str = text.readline()
#             ind = 0
#             count = 1
#             while ind < len(input_str) - 1:
#                 if input_str[ind] == input_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(input_str[ind])
#                     else:
#                         res.write(str(count) + input_str[ind])
#                     count = 1
#                 ind += 1

# compress('file.txt', 'compressedfile')



