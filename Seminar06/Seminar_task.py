def math_string_to_list(s):
    res = []
    s = s.replace(' ', '')
    if s.count('(') != s.count(')'):
        print("Неверная формула!")
        return [1, '+', 1]
    start = -1
    for i in range(len(s)):
        if s[i] == '(' or s[i] in ('*', '/', '+', '-', ')') and s[i - 1] == ')':
            res.append(s[i])
            start = i
        elif s[i] in ('*', '/', '+', '-', ')') and s[i - 1] != ')':
            res.append(int(s[start + 1:i]))
            res.append(s[i])
            start = i
        elif i == len(s) - 1:
            res.append(int(s[start + 1:]))

    return res


def solution(list_):
    result = [int(list_[0])]
    i = 1
    while i < len(list_):
        if list_[i] == '+':
            result.append(list_[i + 1])
        elif list_[i] == '-':
            result.append(list_[i + 1] * -1)
        elif list_[i] == '/':
            result[-1] = result[-1] / list_[i + 1]
        elif list_[i] == '*':
            result[-1] = result[-1] * list_[i + 1]
        i += 2

    return sum(result)


# def math_string(math_list):
#     while ')' in math_list:
#         open_count = 0
#         for i in range(len(math_list)):
#             if math_list[i] == '(':
#                 open_count = i
#             if math_list[i] == ')':
#                 math_list = math_list[0:open_count] + [solution(math_list[open_count + 1:i])] + math_list[i + 1:]
#                 print(math_list)
#                 break
#     return solution(math_list)


def math_string_recurs(math_list):
    if ')' not in math_list:
        return solution(math_list)
    open_count = 0
    for i in range(len(math_list)):
        if math_list[i] == '(':
            open_count = i
        if math_list[i] == ')':
            math_list = math_list[0:open_count] + [solution(math_list[open_count + 1:i])] + math_list[i + 1:]
            print(math_list)
            break
    return math_string_recurs(math_list)


expl = math_string_to_list('((5 + 3) * 4) - 10')
print(expl)
print(math_string_recurs(expl))
