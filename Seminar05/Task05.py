# Продолжаю биться, с этой задачей))

def sequence(list_):
    if not list_:
        return
    res = [list_[0]]
    for i in range(len(list_)):
        if list_[i] > res[-1]:
            res.append(list_[i])
            print(res)
    sequence(list_[1:])


sequence([1, 5, 2, 3, 4, 6, 1, 7])