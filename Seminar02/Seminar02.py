import random


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


# def factorial(n):
#     res = []
#     temp = 1
#     for i in range(1, n + 1):
#         temp *= i
#         res.append(temp)
#     return res
#
#
# print(factorial(5))


# def function(n):
#     arr = []
#     for i in range(1, n + 1):
#         arr.append((1 + 1 / i) ** i)
#     print(arr)
#     return round(sum(arr), 3)
#
#
# print(function(6))


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
# print(create_list(5, 1, 10))


# def random_list(l):
#     print(l)
#     res = []
#     temp = len(l) - 1
#     while temp >= 0:
#         res.append(l.pop(random.randint(0, temp)))
#         temp -= 1
#     return res
#
#
# print(random_list([5, 3, 5, 6, 1, 7, 9, 10]))