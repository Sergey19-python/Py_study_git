#1 Задание 1Урока
number = int(input("Введите целое число: "))
print(number + 2)

#2 Задание 1Урока
number = int(input("Введите число больше 0, но меньше 10: "))
while number >= 10 or number <= 0:
    number = int(input("Введено неверное число, повторите попытку,\nвведите число больше 0, но меньше 10: "))
print(number ** 2)

#3 Задание 1Урока
name = input("Введите имя: ")
familiy = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
ves = int(input("Введите ваш вес: "))

if age <= 30 and (ves >= 50 and ves<= 120):
    print(name, familiy, age, 'лет', ves, 'кг'"- Пациент в хорошем состоянии.")
elif age > 30 and age <= 40 and (ves < 50 or ves > 120):
    print(name, familiy, age, 'лет', ves, 'кг'"- Пациенту требуется заняться собой.")
elif age > 40 and (ves < 50 or ves > 120):
    print(name, familiy, age, 'лет', ves, 'кг'"- Пациенту требуется врачебный осмотр.")
else:
    print(name, familiy, age, 'лет', ves, 'кг'"- Вы относитесь к отдельной категории пациентов, вам следует проконсультироваться с врачом.")

