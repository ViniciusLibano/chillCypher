alphabet = ['abcde','fghjk', 'lmnop', 'qrstu', 'vwxyz']

def encode(text: str):
    clean = ''.join(char for char in text if char.isalnum()).lower()
    for num in '1234567890':
        clean = clean.replace(num, '')
    result = []
    for letter in clean:
        rowIndex = (''.join(alphabet).index(letter)) // 5
        y = rowIndex + 1
        x = alphabet[rowIndex].index(letter) + 1
        result.append(f'{y},{x}')
    
    return ' '.join(result)

def decode(text: str):
    textLi = list(text.split(' '))
    result = ''
    for item in textLi:
        iCoord = list(item.split(','))
        y = int(iCoord[0]) - 1
        x = int(iCoord[1]) - 1
        result += alphabet[y][x]
    return result

teste = 'abc'
c = encode(teste)
d = decode(c)

print(f'{teste}\n{c}\n{d}')