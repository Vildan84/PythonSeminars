'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''

# Первое решение:
# def sum_of_digits():
#     number = input("Enter number: ")
#     result = 0
#     for i in number:
#         if i.isdigit():
#             result += int(i)
#     return result
#
#
# print(sum_of_digits())

# Второе решение:
# def sum_digits_in_number():
#     number = input("Enter number: ")
#     return sum(int(x) for x in number if x.isdigit())
#
#
# print(sum_digits_in_number())

'''
Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
'''
# Первое решение:
# def function(n):
#     arr = []
#     for i in range(1, n + 1):
#         arr.append((1 + 1 / i) ** i)
#     print(arr)
#     return round(sum(arr), 3)
#
#
# print(function(6))


# Второе решение:
# def func(n):
#     return round(sum((1 + 1/i)**i for i in range(1, n + 1)), 3)
#
#
# print(func(6))


'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
'''


# Первое решение:
# def create_list(n, a, b):
#     arr = []
#     for i in range(n * 2 + 1):
#         arr.append(-n + i)
#     print(arr)
#     if a > len(arr) - 1 or b > len(arr) - 1:
#         print("Incorrect index!!!")
#         return
#     return arr[a] * arr[b]
#
#
# print(create_list(5, 1, 10)


# Второе решение:
# def create_list(n, a, b):
#     list_ = [i for i in range(-n, n + 1)]
#     print(list_)
#     return list_[a] * list_[b]
#
#
# print(create_list(7, 4, 5))


'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.
'''
# Первое решение:
# def not_repeat(nums):
#     d = {}
#     for i in nums:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#
#     return [i for i in d if d[i] == 1]
#
#
# print(not_repeat([1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]))


# Второе решение:
def non_repeat(arr):
    return [i for i in arr if arr.count(i) == 1]


print(non_repeat([1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]))