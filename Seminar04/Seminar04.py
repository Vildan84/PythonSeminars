import random

# Первое задание:
# def pi_precision(n):
#     res = 0
#     for i in reversed(range(n)):
#         res += (-1) ** i / (2 * i + 1)
#     return res * 4
#
#
# def pi_precision_short(n):
#     return sum((-1) ** i / (2 * i + 1) for i in reversed(range(n))) * 4
#
#
# print(pi_precision(100000))
# print(pi_precision_short(100000))


# Второе задание:
# def multiplication(n):
#     res = []
#     mul = 2
#     while n > 1:
#         if n % mul == 0:
#             res.append(mul)
#             n /= mul
#         else:
#             mul += 1
#
#     return res
#
#
# print(multiplication(52))


# Третье задание:
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


# Четвертое задание:
# Создаем список из случайных коэфициентов
def random_list(n):
    res = []
    for i in range(n):
        num = random.randint(-20, 20)
        res.append(num)
    return res


list_one = random_list(5)
list_two = random_list(7)

# Формируем многочлен в текстовый файл
def write_poly(nums):
    poly = ''
    for i in range(len(nums) - 1, -1, -1):
        poly += f"{nums[i]}*x^{i}  "
    print(poly)
    return poly


file1 = write_poly(list_one)
file2 = write_poly(list_two)
with open('file1.txt', 'w') as f:
    f.write(file1)
with open('file2.txt', 'w') as f:
    f.write(file2)

# Пятое задание
def read_poly(text):
    with open(text, 'r') as f:
        file = f.read()
        return file


def sum_poly():
    coe_1 = read_poly('file1.txt').split()
    coe_2 = read_poly('file2.txt').split()

    # Формируем список коэфициентов из считанных файлов
    temp_1 = []
    temp_2 = []

    for i in range(len(coe_1)):
        temp_1.append(coe_1[i].split('*')[0])
    for i in range(len(coe_2)):
        temp_2.append(coe_2[i].split('*')[0])

    # Фоормируем список суммированных коэфициентов многочленов
    res = []
    if len(temp_1) > len(temp_2):
        s = len(temp_1) - len(temp_2)
        while s > 0:
            res.append(int(temp_1.pop(0)))
            s -= 1
    if len(temp_2) > len(temp_1):
        s = len(temp_2) - len(temp_1)
        while s > 0:
            res.append(int(temp_2.pop(0)))
            s -= 1

    for i in range(len(temp_1)):
        res.append(int(temp_1[i]) + int(temp_2[i]))

    res.reverse()
    with open('result.txt', 'w') as f:
        f.write(write_poly(res))


print(sum_poly())



