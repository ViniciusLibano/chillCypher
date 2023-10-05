alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(text: str):
    clean = ''.join(char for char in text if char.isalnum()).lower()
    for num in '1234567890':
        clean = clean.replace(num, '')
    iAlpha = ''
    i = -1
    for l in alphabet:
        iAlpha += alphabet[i]
        i = i - 1
    result = ''
    for letter in text:
        result += iAlpha[alphabet.index(letter)]
    return result

print(encode('abc'))