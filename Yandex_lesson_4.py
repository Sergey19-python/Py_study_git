# Задание 1
# number = int(input())
# for i in range(1, number + 1):
#     if i > 1:
#         print()
#     for j in range(1, number + 1):
#         print(f'{i * j}', end=' ')

# Задание 2
# number = int(input())
# for i in range(1, number + 1):
#     for j in range(1, number + 1):
#         print(f'{j} * {i} = {j * i}')

# Задание 3
# number = int(input())
# k = 1
# for i in range(1, number + 1):
#     print(i, end=" ")
#     if i == k * (k + 1) // 2:
#         print()
#         k += 1

# Задание 4
# number = int(input())
# i = 0
# summa = 0
# while i < number:
#     chislo = int(input())
#     while chislo != 0:
#         slog = chislo % 10
#         summa += slog
#         chislo = chislo // 10
#     i +=1
# print(summa)

# Задание 5
# number = int(input())
# flag = False
# count = 0
# i = 0
# while i < number:
#     while (mestnost := input()) != "ВСЁ":
#         if "зайка" in mestnost:
#             flag = True
#     if flag is True:
#         count += 1
#     i += 1
#     flag = False
# print(count)

# Задание 6
# number = int(input())
# a = int(input())
# nod = 0
# i = 1
# while i < number:
#     b = int(input())
#     while nod == 0:
#         if min(a, b) == 1:
#             nod = 1
#         elif min(a, b) == 0:
#             nod = max(a, b)
#         elif a > b:
#             a = a % b
#         elif b > a:
#             b = b % a
#     a = nod
#     nod = 0
#     i += 1
# print(a)

# Задание 7
# number = int(input())
# sec = 3
# i = 0
# for speeder in range(1, number + 1):
#     while sec != 0:
#         print(f"До старта {sec} секунд(ы)")
#         sec -= 1
#     print(f"Старт {speeder}!!!")
#     i += 1
#     sec = 3 + i
    
# Задание 8
# count = int(input())
# winner = ""
# sum_win = 0
# for i in range(count):
#     name = input()
#     number = int(input())
#     summ = 0
#     while number != 0:
#         summ += number % 10
#         number //= 10
#     if sum_win <= summ:
#         sum_win = summ
#         winner = name
# print(winner)

# Задание 9
# count = int(input())
# otvet = ""
# for i in range(count):
#     number = int(input())
#     max_number = 0
#     while number != 0:
#         chislo = number % 10
#         if chislo > max_number:
#             max_number = chislo
#         number //= 10
#     otvet += str(max_number)
# print(otvet)

# Задание 11
# count_chisel = int(input())
# count = 0

# for i in range(count_chisel):
#     number = int(input())
#     if number == 1:
#         continue
#     if number == 2 or number == 3:
#         count += 1
#         continue
#     k = 2
#     flag = False
#     while k ** 2 <= number:
#         if number % k == 0:
#             flag = True
#         k += 1
#     if flag is True:
#         continue
#     else:
#         count += 1
# print(count)

# Задание 12
# height = int(input())
# width = int(input())
# number = height * width
# k = 1
# for i in range(height):
#     if i > 0:
#         print()
#     for j in range(width):
#         if number < 10:
#             print('{:}'.format(k), end=" ")
#         elif number > 9 and number < 100:
#             print('{:2}'.format(k), end=" ")
#         else:
#             print('{:3}'.format(k), end=" ")
#         k += 1
        
# Задание 13
# N = int(input())
# M = int(input())
# chislo = N * M

# k = 1
# for i in range(1, N + 1):
#     if i > 1:
#         print()
#     for j in range(M):
#         if chislo < 10:
#             print('{:1}'.format(k), end=" ")
#         elif chislo > 9 and chislo < 100:
#             print('{:2}'.format(k), end=" ")
#         else:
#             print('{:3}'.format(k), end=" ")
#         k += N
#     k = i + 1

# Задание 14
# N = int(input())
# M = int(input())
# number = N * M
# k = 1
# for i in range(1, N + 1):
#     if i > 1:
#         print()
#     if i % 2 != 0:
#         for j in range(M):
#             if number < 10:
#                 print("{:1}".format(k), end=" ")
#             elif number > 9 and number < 100:
#                 print("{:2}".format(k), end=" ")
#             else:
#                 print("{:3}".format(k), end=" ")
#             k += 1
#         k -= 1
#     else:
#         k += M
#         for a in range(M):
#             if number < 10:
#                 print("{:1}".format(k), end=" ")
#             elif number > 9 and number < 100:
#                 print("{:2}".format(k), end=" ")
#             else:
#                 print("{:3}".format(k), end=" ")
#             k -= 1
#         k = k + M + 1

# Задание 15