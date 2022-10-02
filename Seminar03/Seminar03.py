# def sum_of_negative_index(arr):
#     s = 0
#     for i in range(1, len(arr), 2):
#         s += arr[i]
#     return s


# def sum_of_negative_index_compr(arr):
#     return sum([arr[i] for i in range(1, len(arr), 2)])
#
#
# print(sum_of_negative_index_compr([2, 3, 5, 9, 3, 7, 1, 5]))


# def digits_mult(arr):
#     res = []
#     j = len(arr) - 1
#     if len(arr) % 2 == 0:
#         for i in range(0, len(arr) // 2):
#             res.append(arr[i] * arr[j])
#             j -= 1
#     else:
#         for i in range(0, len(arr) // 2 + 1):
#             res.append(arr[i] * arr[j])
#             j -= 1
#     return res

# Над этим решением пока работаю:
# def digits_mult(arr):
#     return [arr[i] * arr[(i * -1) - 1] for i in range(0, len(arr) // 2)]


# print(digits_mult([2, 3, 5, 7, 1, 5]))


# def find_residual(arr):
#     temp = []
#     for i in arr:
#         if round(i - int(i), 5) > 0:
#             temp.append(round(i - int(i), 5))
#     res = sorted(temp)
#     return res[-1] - res[0]
#
#
# print(find_residual([1.1, 1.2, 5.4, 3.1, 5.001, 10.01]))


# def dec_to_bin(n):
#     res = ''
#     while n > 0:
#         res += str(n % 2)
#         n //= 2
#     return res[::-1]
#
#
# print(dec_to_bin(24))


def fibo(n):
    first_number, second_number = -1, 1
    res = []
    for i in range(n + 1):
        first_number, second_number = second_number, first_number + second_number
        res.append(second_number)
    return res


def fibo_negative(n):
    first_number, second_number = 1, 0
    res = []
    for i in range(n):
        first_number, second_number = second_number, first_number - second_number
        res.append(second_number)
    return res[::-1]


def fibo_and_neg_fibo(n):
    return fibo_negative(n) + fibo(n)


print(fibo_and_neg_fibo(8))





