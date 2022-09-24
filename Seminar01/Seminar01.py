# Task1
# def is_holiday():
#     day = int(input("Введите день недели: "))
#     if day <= 0 or day > 7:
#         print("Wrong number, enter number from 1 to 7")
#     if day == 6 or day == 7:
#         print("Holiday!!!")
#     elif 0 < day < 6:
#         print("Workday(((")
#
#
# print(is_holiday())


# Task2
# def true_or_false(n):
#     res = []
#     result = []
#     for i in range(2 ** n):
#         s = ''
#         for j in range(n):
#             s = str(i % 2) + s
#             i //= 2
#         x = int(s[0])
#         y = int(s[1])
#         z = int(s[2])
#         bool_value_one = bool(not (x or y or z))
#         bool_value_two = bool(not x and not y and not z)
#         res.append(bool_value_one)
#         result.append(bool_value_two)
#         print(s)
#     print(res)
#     print(result)
#     return res == result
#
#
# print(true_or_false(3))


# Task3
# def find_quarter(x, y):
#     if x > 0 and y > 0:
#         print("Dot in first quarter")
#     elif x < 0 and y > 0:
#         print("Dot in second quarter")
#     elif x < 0 and y < 0:
#         print("Dot in third quarter")
#     else:
#         print("Dot in fours quarter")
#
#
# print(find_quarter(3, -3))

# Task4
# def quarter_numbers():
#     number = int(input("Enter quarter number: "))
#     if number <= 0 or number > 4:
#         print("Wrong number, enter number from 1 to 4")
#     if number == 1:
#         print("x = 0, 1, 2, 3, 4..... and y = 0, 1, 2, 3, 4.....")
#     elif number == 2:
#         print("x = 0, -1, -2, -3, -4..... and y = 0, 1, 2, 3, 4.....")
#     elif number == 3:
#         print("x = 0, -1, -2, -3, -4..... and y = 0, -1, -2, -3, -4.....")
#     elif number == 4:
#         print("x = 0, 1, 2, 3, 4..... and y = 0, -1, -2, -3, -4.....")
#
#
# print(quarter_numbers())

# Task5
# def find_distance(a, b):
#     x = a[0] - b[0]
#     y = a[1] - b[1]
#     return round((x ** 2 + y ** 2) ** 0.5, 2)
#
#
# print(find_distance([7, -5], [1, -1]))