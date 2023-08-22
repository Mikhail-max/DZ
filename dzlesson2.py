# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random
# def min_number_coin(number_coins):
#     count_eagle = 0
#     count_tails = 0
#     for i in range(0, number_coins):
#         mass = []
#         mass.append(random.randint(0,1))
#         print(mass, end = " ")
#         if mass == [1]:
#             count_eagle+=1
#             print("count_eagle = ",count_eagle)
#         else:
#             count_tails+=1
#             print("count_tails = ",count_tails)
#     if count_tails >= count_eagle:
#         print(end = "\n")
#         print("Минимальное количество монет, которых нужно перевернуть:  ")
#         return count_eagle
#     else:
#         print(end = "\n")
#         print("Минимальное количество монет, которых нужно перевернуть:  ")
#         return count_tails

    

# number_coins = int(input("Введите количество монет: "))
# print(min_number_coin(number_coins))

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# def number_search(S,P):
#     result = None
#     Y = 0
#     X = 0
#     if S == 0:
#         print("Оба числа равны: 0")
#     if P == 0:
#         Y = 0
#         X = S - Y
#         print("Первое число равно: ", Y)
#         print("Второе число равно: ", X)
#     while P != (S*Y)-(Y**2):
#         if Y == S or Y > 1000:
#             return print("Данные указаны неверно")
#         Y+=1
#     if Y == None:
#         result = "Данные указаны неверно"
#     else:
#         X = S - Y
#         result = print(f"Первое число = {Y}, второе число = {X}")
#     return result

# S = int(input("Введите сумму числа: "))
# P = int(input("Введите произведение числа: "))
# number_search(S,P)

# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.
# def degrees_of_two(N):
#     print(f"Число 2 в степени от 1 до {N} равно: ")
#     i = 1
#     list = []
#     while i <= N:
#         list.append(2**i)
#         i+=1
#     return print(list)

# N = int(input("Введите число: "))
# degrees_of_two(N)

# Задача 1 HARD по желанию Напишите программу, которая принимает на вход целое или дробное число 
# и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

# def number_of_digits(number):
#     print(f"Цифр в числе {number}: ")
#     count = 0
#     if number != number // 1:
#         while number // 1 < number:
#             number = number * 10
#     while number > 0:
#         number = number // 10
#         count+=1
        
    
#     return print(count)

# number = float(input("Введите число: "))
# number_of_digits(number)

# Задача VERY HARD необязательная
# Имеется список случайных целых чисел. 
# Создайте список, в который попадают числа, 
# описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть 
# числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь 
# есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

import random

def max_increasing_sequence(number_elements, min, max):
    list = []
    i = 1
    sequence = 0
    max_sequence = 0
    while i <= number_elements:
        list.append(random.randint(min,max))
        i+=1
    
    min_number = 0
    max_number = 0
    min_number_sequence = 0
    max_number_sequence = 0
    k = 0
    h = 1
    i = 1
    while i <= number_elements:
        if list[k]+1 == list[h]:
            if min_number == 0:
                min_number = list[k]
            if min_number > list[k]:
                min_number = list[k]
            k = h
            if max_number < list[k]:
                max_number = list[k]
            h = 0
            sequence+=1
        else:
            h+=1
            if h == number_elements:
                if max_sequence < sequence:
                    max_number_sequence = max_number
                    min_number_sequence = min_number
                    max_sequence = sequence
                    sequence = 0
                    min_number = 0
                    max_number = 0
                else:
                    sequence = 0
                i+=1
                h = 0
                k = i - 1
                
    list_sequence = [min_number_sequence,max_number_sequence]
    
    return(print(f"{list} => {list_sequence}так как здесь вразброс присутствуют все числа от {min_number_sequence} до {max_number_sequence}"))


number_elements = int(input("Введите количество элементов в последовательности: "))
min = int(input("Введите минимальный диапазон списка: "))
max = int(input("Введите максимальный диапазон списка: "))
max_increasing_sequence(number_elements, min, max)