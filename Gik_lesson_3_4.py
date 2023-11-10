
# Программа, которая угадывает загаданное число пользователем.
# import random

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# otvet = ""

# while True:
#     number = random.randint(a, b)
#     print(number)
#     otvet = input("Введите ответ: ")
#     if otvet == "=":
#         print("Комьютер угадал !!!")
#         break
#     elif otvet == "<":
#         b = number - 1
#     else:
#         a = number + 1

# Задача_1
# def information(name, age, city):
#     string = (f"{name}, {age} год(а), проживающий в городе {city}" )
#     return string

# a = information("Inna", 20, "Abakan")
# print(a)

#Задача_2
# def maximum(a, b, c):
#     return max(a, b, c)

# number = maximum(5,8,99)
# print(number)

# #Задача_3
# name_igrok = input("Введите имя игрока: ")
# igrok = {
#     "name":name_igrok,
#     "health":100,
#     "damage":50, 
#     "armor":1.2
# }

# name_vrag = input("Введите имя врага: ")
# vrag = {
#     "name":name_vrag,
#     "health":100,
#     "damage":50,
#     "armor":1.4
# }

# def bron(napad, otraz):
#     return napad / otraz

# def attak(napad, otraz):
#     otraz["health"] -= bron(napad["damage"], otraz["armor"])


# attak(napad=vrag, otraz=igrok)
# print(igrok)

# attak(napad=igrok, otraz=vrag)
# print(vrag)
