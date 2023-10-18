# 2.1
# Первое задание
# name = "Яндекс"
# print(f'Привет, {name}!')

# Второе задание
# print('Как Вас зовут?')
# name = input()
# print('Привет,', name)
#
# # Третье задание
# message = input()
# print(f'{message}')
# print(f'{message}')
# print(f'{message}')
#
# # Четвертое задание
# m = int(input())
# s = 2.5 * 38
# print(int(m - s))
#
# # Пятое задание
# cena = int(input())
# ves = int(input())
# many = int(input())
# summa = (many - (cena * ves))
# print(summa)
#
# # Шестое задание
# tovar = input()
# cena = int(input())
# ves = int(input())
# many = int(input())
# itog = cena * ves
# sdacha = many - itog
# print(f"Чек\n{tovar} - {ves}кг - {cena}руб/кг")
# print(f"Итого: {itog}руб\nВнесено: {many}руб\nСдача: {sdacha}руб")
#
# # Седьмое задание
# number = int(input())
# print("Купи слона!\n" * number)
#
# # Восьмое задание
# number = int(input())
# message = input()
# print(f'Я больше никогда не буду писать "{message}"!\n' * number)
#
# # Девятое задание
# time = int(input())
# chaild_count = int(input())
# sousage_count = int((time / 2) * chaild_count)
# print(sousage_count)

# Деcятое задание
# name = input()
# closed = int(input())
# group = closed // 100
# number = closed % 10
# bed = (closed % 100) // 10
# print(f"Группа №{group}.\n{number}. {name}.\nШкафчик: {closed}.\nКроватка: {bed}.")

# # Одиннадцатое задание
# number = int(input())
# one = number // 1000
# too = (number % 1000) // 100
# three = (number % 100) // 10
# four = number % 10
# print(too,one,four,three, sep='')

# # Двенадцатое задание
# string_one = int(input())
# string_too = int(input())
# # Расчёт первой строки
# one_first = string_one // 100
# too_first = (string_one % 100) // 10
# three_first = string_one % 10
# # Расчёт второй строки
# one_second = string_too // 100
# too_second = (string_too % 100) // 10
# three_second = string_too % 10
# # Считаем сумму
# three = (three_first + three_second) % 10
# too = (too_first + too_second) % 10
# one = (one_first + one_second) % 10
# print(one, too, three, sep='')

# # Тринадцатое задание
# chield = int(input())
# bon = int(input())
# bon_one_chield = int(((bon / chield) * 10) // 10)
# ostatok_bon = bon - (bon_one_chield * chield)
# print(f'{bon_one_chield}\n{ostatok_bon}')

# Четырнадцатое задание
n_child = int(input())
total = int(input())
print(total // n_child)
print(total % n_child)