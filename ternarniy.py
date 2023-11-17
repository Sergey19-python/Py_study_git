# Задание_1
spisok_1 = ["apple", "apple", "banana", "oringe", "ananas", "cherry", "limon", "kiwi"]
spisok_2 = ["strawberry", "apple", "ananas", "kiwi"]

result = [fruit for fruit in spisok_2 if fruit in spisok_1]
print(result)



# Задание_2
numbers = [1,4,-2,6,9,77,8,-44,33,-13,12,24,48,-7,-12,90]

number_1 = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0 ]
print(number_1)



# Задание_3

numb = [1,4,-2,6,9,77,8,-44,33,-13,12,24,48,-7,-12,90]
      
def generation(list):
    import math
    list_1 = list[:]
        
    gen_list = [math.sqrt(number) if number > 0 else number for number in list_1]
    return gen_list

print(generation(numb))
print(numb)



# Задание_4

def chislo(number):
    if number == 13:
        raise ValueError ("Введено число 13")
    elif number < 1 or number > 100:
        raise Exception ("Введено несоответствующее условиям число")
    else:
        return number ** 2
    
    
numb = int(input("Введите число: "))
try:
    print(chislo(numb))
except ValueError:
    print("Введите число от 1 до 100, кроме 13")
except Exception:
    print("Значение не соответствует условиям, введите число от 1 до 100, кроме 13")