let = "aaaaaaabbbbbbbbbbbbbbbbccccc11111mmmm5555555555"

with open('rle_input', 'w') as f:
    f.write(let)
with open('rle_input', 'r') as f:
    letters = f.read()
print(letters)


def coding(s):
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        if s[i] != s[i - 1]:
            res.append(str(count))
            res.append(s[i - 1])
            count = 1
        if count == 10:
            res.append(str(count - 1))
            res.append(s[i - 1])
            count = 1
        if i + 1 == len(s):
            res.append(str(count))
            res.append(s[i])
            break
    return ''.join(res)


with open('rle_coded', 'w') as f:
    f.write(coding(letters))
with open('rle_coded', 'r') as f:
    coded = f.read()
print(coded)


def encoding(code):
    result = []
    for i in range(0, len(coded), 2):
        result.append(int(coded[i]) * coded[i + 1])
    return ''.join(result)


with open('rle_encoded', 'w') as f:
    f.write(encoding(coded))
with open('rle_encoded', 'r') as f:
    encoded = f.read()
print(encoded)