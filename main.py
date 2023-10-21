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

# # Четырнадцатое задание
# n_child = int(input())
# total = int(input())
# print(total // n_child)
# print(total % n_child)

# # Пятнадцатое задание
# chasy = int(input())
# minute = int(input())
# minute_dostavka = int(input())
# minuteostatka = ((chasy * 60) + minute + minute_dostavka) % 60
# chasyostatka = (((chasy * 60) + minute + minute_dostavka) // 60) % 24
# print(f'{chasyostatka:02}:{minuteostatka:02}') # Можно вывести количество разрядов

# Шестнадцатое задание
# punkt_a = int(input())
# punkt_b = int(input())
# speed = int(input())
# time = (punkt_b - punkt_a) / speed
# print(f'{time:.2f}')

# Семнадцатое задание
# desyt = int(input())
# doubl = input()
# perevod = int(doubl, 2)
# print(perevod + desyt)

# Восемнадцатое задание
# cena = input()
# many = int(input())
# perevod = int(cena, 2)
# sdacha = many - perevod
# print(sdacha)

# Девятнадцатое задание
# tovar = input()
# cena = int(input())
# ves = int(input())
# many = int(input())
# itog = cena * ves
# sdacha = many - itog
# print(f"{'Чек':=^35}")
# print('Товар:', f"{tovar}".rjust(35-7))
# print('Цена:', f"{ves}кг * {cena}руб/кг".rjust(35-6))
# print('Итого:', f"{itog}руб".rjust(35-7))
# print('Внесено:', f"{many}руб".rjust(35-9))
# print('Сдача:', f"{sdacha}руб".rjust(35-7))
# print('=' * 35)

# Двадцатое задание
# Формула:
# 32 кг общий вес
# 285 общая цена за кг
# 300 цена за кг первого вида
# 240 цена за кг второго вида
# кг каждого вида - ?
# (32 * 285 - 32 * 240) / (300 - 240) от общей прибыли отнимаем прибыль за первый вид котлет и делим
# на разницу между стоимостью видов котлет, потом отнимаем от общей массы найденный вес первого вида и находим кг второго вида

ves = int(input())
cena_za_kg = int(input())
cena_first = int(input())
cena_second = int(input())
ves_second = int((ves * cena_za_kg - ves * cena_second) / (cena_first - cena_second))
ves_first = ves - ves_second
print(ves_second, ves_first, sep=' ')