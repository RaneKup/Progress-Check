#уровень B
#Зайцев Егор ии-72
#задача 3

import random
#создаём пустой список
nums = []
#создаём случайные значения
for i in range(6):
    nums.append(random.randint(1,24))
#создаём переменную чисел для вывода
count = 0
#проверяем числа на кратность 3
for i in nums:
    if i % 3 == 0:
        count += 1
#выводим результат
print(count)

#задача 2
#ввод числа
n = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))
n4 = int(input('Введите четвёртое число: '))
n5 = int(input('Введите пятое число: '))
n6 = int(input('Введите шестое число: '))

#создаём список
nums = [n, n2, n3, n4, n5, n6]

#проверяем числа
numbersP = list(filter(lambda x: x > 0, nums))
numbersM = list(filter(lambda x: x < 0, nums))

#получаем количество чёт/нечёт чисел
Lp = len(numbersP)
Lm = len(numbersM)

#выводим результат
print(Lp)
print(Lm)
