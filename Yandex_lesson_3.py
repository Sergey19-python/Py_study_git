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
