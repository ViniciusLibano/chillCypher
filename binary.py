def decToBinary(num: int):
    binaryLi = []
    while num > 0:
        if num <= 1:
            binaryLi.append(num)
            num = 0
        else:
            binaryLi.append(num%2)
            num = num // 2
    invertText = ''
    for item in binaryLi:
        invertText += str(item)

    binaryText = ''
    i = -1
    for letter in invertText:
        binaryText += invertText[i]
        i = i - 1

    return binaryText

def encode(text: str):
    result = []
    for letter in text:
        asc = ord(letter)
        result.append(decToBinary(asc))

    return ' '.join(result)

def decode(text: str):
    l = []
    for binary in text:
        l.append(int(binary))

    result = 0
    for ln in range(len(l)-1, -1, -1):
        result = result + (l[ln] * pow(2, ln))

    print(result)


decode('1000001')
print(encode('A'))