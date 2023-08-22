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