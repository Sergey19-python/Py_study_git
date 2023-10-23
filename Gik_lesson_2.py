# ЗАДАЧА 1: Даны два произвольные списка. Удалите из первого списка
# элементы присутствующие во втором списке.

# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ:
# Решение: Программа проходит по каждому элементу первого списка и
# проверяет наличие подобного числа во втором списке,
# если совпадений нет, то число добавляется в новый третий список.
my_list_1 = [2, 2, 2, 2, 7, 7, 7, 5, 9, 9, 9, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3, 9]
my_list_3 = []

for i in range(len(my_list_1)):
    if my_list_1[i] not in my_list_2:
        my_list_3.append(my_list_1[i])
my_list_1 = my_list_3
print(my_list_1)


# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ:
# Решение: Программа проходит по каждому элементу среза первого
# списка и если находит совпадения во втором списке, то удаляет
# число в реальном списке.
my_list_1 = [2, 2, 2, 2, 7, 7, 7, 5, 9, 9, 9, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3, 9]

for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)

# ЗАДАЧА 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например:
# второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ:
data = input("Введите дату в формате 'dd.mm.yyyy': ")
srez_day = data[:2]
srez_mesyc = data[3:5]
srez_god = data[6:10]
day_print = ''
mesyc_print = ''
day = {
    '01':'первое', '02':'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одиннадцатое'
}
mesyc = {
    '01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня', '07':'июля',
    '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря'
}
for day_d in day.keys():
    if day_d == srez_day:
        day_print = day[day_d]
for mesyc_d in mesyc.keys():
    if mesyc_d == srez_mesyc:
        mesyc_print = mesyc[mesyc_d]

print(f"{day_print} {mesyc_print} {srez_god} года.")





# ЗАДАЧА 3:Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ:
# Перебираем циклом каждый элемент первого списка и проверяем
# количество таких элементов в списке, если кол-во = 1,
# то добавляем этот элемент в новый список.
list_1 = [8, 1, 1, 2, 2, 2, 4, 6, 7, 7, 9, 8]
list_2 = []
for i in range(len(list_1)):
    if list_1.count(list_1[i]) == 1:
        list_2.append(list_1[i])
print(list_2)



