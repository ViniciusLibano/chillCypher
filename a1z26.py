alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(text: str):
    clean = ''.join(char for char in text if char.isalnum()).lower()
    for num in '1234567890':
        clean = clean.replace(num, '')
    result = []
    for letter in clean:
        result.append(str(alphabet.find(letter) + 1))
    return '-'.join(result)

def decode(text: str):
    textLi = text.split('-')
    result = ''
    for num in textLi:
        i = int(num) - 1
        result += alphabet[i]
    return result

texto = 'teste muito foda!'
cript = encode(texto)
decript = decode(cript)

print(f'{texto}\n{cript}\n{decript}')