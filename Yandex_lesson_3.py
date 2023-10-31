# Задание_1
# while (stroka := input()) != "Три!":
#     print("Режим ожидания...")
# print("Ёлочка, гори!")

# Задание_2
# number = 0
# while (stroka := input()) != "Приехали!":
#     if "зайка" in stroka:
#         number += 1
# print(number)

# Задание_3
# n = int(input())
# k = int(input())
# for number in range(n, k+1):
#     print(number, end=" ")

# Задание_4
# n = int(input())
# k = int(input())
# if n < k:
#     for number in range(n, k+1):
#         print(number, end=" ")
# else:
#     for number in range(n, k-1, -1):
#         print(number, end=" ")

# Задание_5
# itog = 0
# while (stoimost := float(input())) != 0:
#     if stoimost >= 500:
#         itog += stoimost * 0.9
#     else:
#         itog += stoimost
# print(itog)

# Задание_6
# one = int(input())
# two = int(input())
# nod = 0
# while nod == 0:
#     if min(one, two) == 1:
#         nod = 1
#     elif one == 0 or two == 0:
#         nod = max(one, two)
#     elif one > two:
#         one = one % two
#     elif two > one:
#         two = two % one
# print(nod)

# Задание_7
# one = int(input())
# two = int(input())
# i = 1
# while True:
#     if i % one == 0 and i % two ==0:
#         break
#     else:
#         i +=1
# print(i)

# Задание_8
# stroka = input()
# number = int(input())
# print(f'{stroka}\n' * number)

# Задание_9
# number = int(input())
# factorial = 1
# for i in range(1, number + 1):
#     factorial = factorial * i
# print(factorial)

# Задание_10
# x = 0
# y = 0
# while (napravlenie := input()) != "СТОП":
#     shagi = int(input())
#     if "СЕВЕР" in napravlenie:
#         y = y + shagi
#     if "ЮГ" in napravlenie:
#         y = y - shagi
#     if "ЗАПАД" in napravlenie:
#         x = x - shagi
#     if "ВОСТОК" in napravlenie:
#         x = x + shagi
# print(f'{y}\n{x}')

# Задание_11
# chislo = input()
# spisok_number = []
# for i in range(len(chislo)):
#     spisok_number.append(chislo[i])
# summa = list(map(int, spisok_number))
# print(sum(summa))

# Задание_12
# chislo = input()
# spisok_number = []
# for i in range(len(chislo)):
#     spisok_number.append(chislo[i])
# maximum = max(list(map(int, spisok_number)))
# print(maximum)

# Задание_13
# number = int(input())
# first_gamer = input()
# first_gamer_two = ""
# i = 1
# while i < number:
#     first_gamer_two = input()
#     if first_gamer_two < first_gamer:
#         first_gamer = first_gamer_two
#     i +=1
# print(first_gamer)

# # Задание_14
# number = int(input())
# otvet = True
# i = 2

# if number == 1:
#     print("NO")
# elif number == 2 or number == 3:
#     print("YES")
# else:
#     while i ** 2 < number or i ** 2 == number:
#         if number % i == 0:
#             otvet = False
#             break
#         else:
#             i += 1
#
#     if otvet is True:
#         print("YES")
#     else:
#         print("NO")

# Задание_15
# number = int(input())
# i = 0
# count = 0
# stroka = ""
# while i < number:
#     stroka = input()
#     if "зайка" in stroka:
#         count += 1
#     i += 1
# print(count)

# # Задание_16
# number = input()
# if number[::1] == number[::-1]:
#     print("YES")
# else:
#     print("NO")

# Задание_17
# number = input()
# number_list = []
# for i in range(len(number)):
#     number_list.append(number[i])
# number_list = list(map(int, number_list))
#
# for chislo in number_list[:]:
#     if chislo % 2 == 0:
#         number_list.remove(chislo)
# str_number_list = [str(n) for n in number_list]
# str_number_list = "".join(str_number_list)
# print(str_number_list)

# Задание_18
# number = int(input())
# list = []
# d = 2
# while d ** 2 <= number:
#     if number % d == 0:
#         list.append(d)
#         number //= d
#     else:
#         d +=1
# if number > 1:
#     list.append(number)
# print(" * ".join(str(ls) for ls in list))

# Задание_19
chislo = int(input())
i = 0
while i < 10:
    number = int(input())
    if number < chislo:
        print("Больше")
    elif number > chislo:
        print("Меньше")
    else:
        print("Угадал!")
        break
    i += 1