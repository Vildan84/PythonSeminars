with open('file1.txt', 'w') as f:
    f.write("абвгдб собака абв нокабв пришла дабв домой")

with open('file1.txt', 'r') as f:
    s = f.read().split()


def del_letters(st):
    return ' '.join(list(filter(lambda x: 'абв' not in x, st)))


print(del_letters(s))