# 2.1
# Первое задание
name = "Яндекс"
print(f'Привет, {name}!')

# Второе задание
print('Как Вас зовут?')
name = input()
print('Привет,', name)

# Третье задание
message = input()
print(f'{message}')
print(f'{message}')
print(f'{message}')

# Четвертое задание
m = int(input())
s = 2.5 * 38
print(int(m - s))

# Пятое задание
cena = int(input())
ves = int(input())
many = int(input())
summa = (many - (cena * ves))
print(summa)

# Шестое задание
tovar = input()
cena = int(input())
ves = int(input())
many = int(input())
itog = cena * ves
sdacha = many - itog
print(f"Чек\n{tovar} - {ves}кг - {cena}руб/кг")
print(f"Итого: {itog}руб\nВнесено: {many}руб\nСдача: {sdacha}руб")

# Седьмое задание
number = int(input())
print("Купи слона!\n" * number)