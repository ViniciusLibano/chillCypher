alphabet = 'abcdefghijklmnopqrstuvwxyz'

invert = ''
i = -1
for l in alphabet:
    invert += alphabet[i]
    i = i - 1

def encode(text: str):
    clean = ''.join(char for char in text if char.isalnum()).lower()
    for num in '1234567890':
        clean = clean.replace(num, '')
    result = ''
    for letter in text:
        result += invert[alphabet.index(letter)]
    return result

def decode(text: str):
    result = ''
    for letter in text:
        result += alphabet[invert.index(letter)]
    return result