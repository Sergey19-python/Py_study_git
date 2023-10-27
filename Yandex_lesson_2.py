# # Задание 1
# print("Как Вас зовут?")
# name = input()
# print(f'Здравствуйте, {name}!')
# print("Как дела?")
# dela = input()
# if dela == "хорошо":
#     print("Я за вас рада!")
# else:
#     print("Всё наладится!")
#
# # Задание 2
# speed_pet = int(input())
# speed_vas = int(input())
# if speed_pet > speed_vas:
#     print("Петя")
# else:
#     print("Вася")

# # Задание 3
# speed_pet = int(input())
# speed_vas = int(input())
# speed_tol = int(input())
# if speed_pet > speed_vas and speed_pet > speed_tol:
#     print("Петя")
# elif speed_vas > speed_tol:
#     print("Вася")
# else:
#     print("Толя")

# Задание 4
# speed_pet = int(input())
# speed_vas = int(input())
# speed_tol = int(input())
#
# if speed_vas > speed_pet and speed_vas > speed_tol:
#     print("1. Вася")
#     if speed_pet > speed_tol:
#         print("2. Петя\n3. Толя")
#     else:
#         print("2. Толя\n3. Петя")
#
# elif speed_pet > speed_vas and speed_pet > speed_tol:
#     print("1. Петя")
#     if speed_vas > speed_tol:
#         print("2. Вася\n3. Толя")
#     else:
#         print("2. Толя\n3. Вася")
#
# else:
#     speed_tol > speed_vas and speed_tol > speed_pet
#     print("1. Толя")
#     if speed_vas > speed_pet:
#         print("2. Вася\n3. Петя")
#     else:
#         print("2. Петя\n3. Вася")

# # Задание 5
# N = int(input())
# M = int(input())
# pety = 7
# vasy = 6
# pety_count = (pety - 3) + 2 + N
# vasy_count = vasy + 3 + 3 + M
# if pety_count > vasy_count:
#     print("Петя")
# else:
#     print("Вася")

# # Задание 6
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("YES")
# else:
#     print("NO")

# # Задание 7
# number = int(input())
# one = str(number // 1000)
# two = str((number // 100) % 10)
# three = str((number // 10) % 10)
# four = str(number % 10)
# number_two = int(four + three + two + one)
# if number == number_two:
#     print("YES")
# else:
#     print("NO")

# Задание 8
# text = input()
# if "зайка" in text:
#     print("YES")
# else:
#     print("NO")

# Задание 9
# name_one = input()
# name_two = input()
# name_three = input()
# if (name_one < name_two) and (name_one < name_three):
#     print(name_one)
# elif name_two < name_three:
#     print(name_two)
# else:
#     print(name_three)

# # Задание 10
# password = int(input())
# one = int(password // 100)
# two = int((password // 10) % 10)
# three = int(password % 10)
# one_new = (two + three)
# two_new = (one + two)
# if one_new > two_new:
#     new_password = str(one_new) + str(two_new)
# else:
#     new_password = str(two_new) + str(one_new)
# print(int(new_password))

# Задание 11
# number = int(input())
# one = int(number // 100)
# two = int((number // 10) % 10)
# three = int(number % 10)
# minimum = min(one, two, three)
# maximum = max(one, two, three)
# sred = (one + two + three) - (minimum + maximum)
# if sred * 2 == minimum + maximum:
#     print("YES")
# else:
#     print("NO")

# Задание 12
# a = int(input())
# b = int(input())
# c = int(input())
# if a < (b + c) and b < (a + c) and c < (b + a):
#     print("YES")
# else:
#     print("NO")

# Задание 13
# a = int(input())
# b = int(input())
# c = int(input())
# a_one = a // 10
# a_two = a % 10
# b_one = b // 10
# b_two = b % 10
# c_one = c // 10
# c_two = c % 10
# if (a_one == b_one) and (b_one == c_one):
#     print(a_one)
# else:
#     print(a_two)

# Задание 14
# number = int(input())
# one = number // 100
# two = (number // 10) % 10
# three = number % 10
# minimum = min(one, two, three)
# maximum = max(one, two, three)
# sred = (one + two + three) - (minimum + maximum)
# if minimum == 0:
#     min_print = str(sred) + str(minimum)
# else:
#     min_print = str(minimum) + str(sred)
# max_print = str(maximum) + str(sred)
# print(f'{min_print} {max_print}')

# Задание 15
# one = int(input())
# two = int(input())
# one_a = one // 10
# one_b = one % 10
# two_a = two // 10
# two_b = two % 10
# minimum = min(one_a, one_b, two_a, two_b)
# maximum = max(one_a, one_b, two_a, two_b)
# sredney = ((one_a + one_b + two_a + two_b) - (minimum + maximum)) % 10
# otvet = str(maximum) + str(sredney) + str(minimum)
# print(otvet)

# Задание 16
# pety = int(input())
# vasy = int(input())
# toly = int(input())
# one = ""
# two = ""
# three = ""
# if pety > vasy and pety > toly:
#     one = 'Петя'
#     if vasy > toly:
#         two = 'Вася'
#         three = 'Толя'
#     else:
#         two = 'Толя'
#         three = 'Вася'
# elif vasy > pety and vasy > toly:
#     one = 'Вася'
#     if pety > toly:
#         two = 'Петя'
#         three = 'Толя'
#     else:
#         two = 'Толя'
#         three = 'Петя'
# elif toly > vasy and toly > pety:
#     one = 'Толя'
#     if vasy > pety:
#         two = 'Вася'
#         three = 'Петя'
#     else:
#         two = 'Петя'
#         three = 'Вася'
# print(f'{one}'.center(24))
# print(f'  {two}'.ljust(24))
# print(f'{three}'.rjust(22))
# print("   II", "I", "III", sep="      ")

# # Задание 17
# a = float(input())
# b = float(input())
# c = float(input())
# D = (b ** 2) - (4 * a * c)
# if D > 0:
#     x1 = (-b + D ** 0.5) / (2 * a)
#     x2 = (-b - D ** 0.5) / (2 * a)
#     if x1 < x2:
#         print(f'{x1:.2f} {x2:.2f}')
#     else:
#         print(f'{x2:.2f} {x1:.2f}')
# elif D == 0:
#     x1 = -b / (2 * a)
#     print(f'{x1:.2f}')
# else:
#     print("No solution")



# Задание 18
# a = int(input())
# b = int(input())
# c = int(input())
# max_storona = max(a, b, c)
# min_storona = min(a, b, c)
# ostalnye = (a + b + c) - (max_storona + min_storona)
# if max_storona ** 2 == (min_storona ** 2) + (ostalnye ** 2):
#     print("100%")
# elif max_storona ** 2 < (min_storona ** 2) + (ostalnye ** 2):
#     print("крайне мала")
# else:
#     print("велика")



# Задание 20
# string_one = input()
# string_two = input()
# string_three = input()
# fraza = "зайка"
# stroka_print = ""
# dlina = len(string_one)
# if fraza in string_one:
#     stroka_print = string_one
#     dlina = len(string_one)
# if fraza in string_two:
#     if string_two < stroka_print or stroka_print == "":
#         stroka_print = string_two
#         dlina = len(string_two)
# if fraza in string_three:
#     if string_three < stroka_print or stroka_print == "":
#         stroka_print = string_three
#         dlina = len(string_three)
# print(f'{stroka_print} {dlina}')
