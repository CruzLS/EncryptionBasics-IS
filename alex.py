import sys
import playfair

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifrar():
    while True:
        print(
            """
            1. Cifrar Vigenere
            2. Decifrar Vigenere
            3. Cifrar Playfair
            4. Decifrar Playfair
            5. Salir
            """
        )
        opt = input("¿Qué deseas hacer? ")
        if opt=="1":
            print (cifrar_vigenere())
        elif opt=="2":
            print (decifrar_vigenere())
        elif opt=="3":
            print( cifrar_plaifair())
        elif opt=="4":
            print(decifrar_playfair())
        elif opt=="5":
            print("Bye")
            sys.exit()
        else:
            print("Opcion invalida.")

def cifrar_vigenere():
    key = input("Llave:")
    message = input("Mensaje:")
    return translate_vigenere(key, message, 'encrypt')

def decifrar_vigenere():
    key = input("Llave:")
    message = input("Mensaje:")
    return translate_vigenere(key, message, 'decrypt')

from pycipher import Playfair
def cifrar_plaifair():
    return Playfair(input("Llave:")).encipher(input("Mensaje:"))

def decifrar_playfair():
    return Playfair(input("Llave:")).decipher(input("Mensaje:"))

def translate_vigenere(key, message, mode):
    translated = []  # stores the encrypted/decrypted message string
    keyIndex = 0
    key = key.upper()
    for symbol in message:  # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # subtract if decrypting
            num %= len(LETTERS)  # handle the potential wrap-around
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1  # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

if __name__ == '__main__':
    cifrar()