def binary(num: int):
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
        result.append(binary(asc))

    return ' '.join(result)

def decode(text: str):
    

print(encode('ABC'))