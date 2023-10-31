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
number = int(input())
a = int(input())
nod = 0
i = 1
while i < number:
    b = int(input())
    while nod == 0:
        if min(a, b) == 1:
            nod = 1
        elif min(a, b) == 0:
            nod = max(a, b)
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a
    a = nod
    nod = 0
    i += 1
print(a)