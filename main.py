# -*- coding: utf-8 -*-

import os
import string
import re
import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TAM_MAX_CLAVE = 26

def __init__(self):
    pass

def cifrar():
    textoCifrado = ''
    key = ''
    ans=True
    while ans:
        print ("""
        1. Cifrar Alberti
        2. Descifrar Alberti
        3. Cifrado Hill
        4. Descifrar Hill
        5. Cifrar Vigenere
        6. Decifrar Vigenere
        7. Cifrar Playfair
        8. Decifrar Playfair
        9. Cesar (Cifrar - Descifrar)
        10. Polybius
        X. Salir
        """)
        ans=input("¿Qué deseas hacer? ")
        if ans=="1":
            print (cifrar_alberti())
        elif ans=="2":
            print (descifrar_alberti())
        elif ans=="3":
            bandera = True
            key = "GYBNQKURPGYBNQKU"
            while bandera:
                mensaje = input('¿Cuál es el mensaje que desea cifrar? ').upper()
                if not mensaje.isdigit():
                    bandera = False
                else:
                    print ("Ingrese sólo letras")
                    bandera = True
            cipherText = cifrado_hill(mensaje, key)
            print ("\n Mensaje cifrado: " +cipherText)
            bandera = True
        elif ans=="4":
            while bandera:
                cipherText = input('¿Cuál es el mensaje que desea cifrar? ').upper()
                if not cipherText.isdigit():
                    bandera = False
                else:
                    print ("Ingrese sólo letras")
                    bandera = True
            decipherText = cifrado_hill(cipherText, key, True)
            if decipherText.find('|') > -1 : decipherText = decipherText[:decipherText.find('|')]
            print ("\n Mensaje descifrado: " +decipherText)
        elif ans=="5":
            print (cifrar_vigenere())
        elif ans=="6":
            print (decifrar_vigenere())
        elif ans=="7":
            print( cifrar_plaifair())
        elif ans=="8":
            print(decifrar_playfair())
        elif ans=="9":
            def obtenerModo():
                while True:
                    print('¿Deseas encriptar o desencriptar un mensaje?')
                    modo = input().lower()
                    if modo in 'encriptar e desencriptar d'.split():
                        return modo
                    else:
                        print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')
           

            def obtenerMensaje():
                print('Ingresa tu mensaje:')
                return input()

            def obtenerClave():
                clave = 0
                while True:
                    print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
                    clave = int(input())
                    if (clave >= 1 and clave <= TAM_MAX_CLAVE):
                        return clave

            def obtenerMensajeTraducido(modo, mensaje, clave):
                if modo[0] == 'd':
                    clave= -clave
                traduccion = ''

                for simbolo in mensaje:
                    if simbolo.isalpha():
                        num = ord(simbolo)
                        num += clave

                        if simbolo.isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif simbolo.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):

                                num += 26
                        traduccion += chr(num)

                    else:
                        traduccion += simbolo

                return traduccion

            modo = obtenerModo()

            mensaje = obtenerMensaje()

            clave = obtenerClave()

            print('Tu texto traducido es:')

            print(obtenerMensajeTraducido(modo, mensaje, clave))       
        elif ans=="10":    
            def __prepare_sentence__(self, sentence):
                """Prepare a sentence for the encryption"""
                accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
                ascii = ["A", "E", "I", "O", "U", "C"]
                
                i = 0
                for word in accent: # Replacing accented characters possible
                    for letter in word:
                        sentence = sentence.replace(letter, ascii[i])
                    i += 1
                for letter in "',-;:!?.":  # Remove punctuation
                    sentence = sentence.replace(letter, "")
                sentence = sentence.upper()  # Passage in capitals letters
                return sentence

            def encipher(self, to_encrypt):
                """Encipher a plaintext"""
                List_H, List_V = [], []
                for j in range(4):
                    for i in range(5):
                        List_H.append(chr(65+5*j+i))
                    List_V.append(List_H)
                    List_H = []
                List_H = []
                List_H.append(chr(85))
                List_H.append(chr(86))
                List_H.append(chr(88))
                List_H.append(chr(89))
                List_H.append(chr(90))
                List_V.append(List_H)
                
                to_encrypt = self.__prepare_sentence__(to_encrypt)
                to_encrypt = to_encrypt.replace(" ", "")  # Remove the space
                
                for i in range(len(to_encrypt)):
                    pos = ord(to_encrypt[i])-65
                    verti = str(int((pos/5)+1))
                    hori = str((pos % 5)+1)
                    fin = verti + hori
                    print (fin, end=' ')
                print()

            def decipher(self, to_decrypt):
                """Decipher a ciphertext"""
                List_H, List_V = [], []
                for j in range(4):
                    for i in range(5):
                        List_H.append(chr(65+5*j+i))
                    List_V.append(List_H)
                    List_H = []
                List_H = []
                List_H.append(chr(85))
                List_H.append(chr(86))
                List_H.append(chr(88))
                List_H.append(chr(89))
                List_H.append(chr(90))
                List_V.append(List_H)

                to_decrypt = to_decrypt.replace(" ", "")  # Remove the space
                length = len(to_decrypt)
                
                for h in range(0, length, 2):
                    pos = int(to_decrypt[h])-1
                    pos2 = int(to_decrypt[h+1])-1
                    carac = List_V[pos][pos2]
                    print(carac, end='')
            print()
        elif ans=="X":
            print("\n Bye...")
            sys.exit()
        elif ans !="":
            print("\n Opción no valida, intenta nuevamente")

def cifrar_alberti():
    mensaje_cifrado = ''
    bandera = True

    while bandera == True:    
        mensaje = input('¿Cuál es el mensaje que desea cifrar? ').upper()
        if not mensaje.isdigit():
            bandera = False
        else:
            print ("Ingrese sólo letras")
            bandera = True

    bandera = True
    
    while bandera == True:
        clave = input('¿Cuál es la clave que desea utilizar para el mensaje? ').upper()
        if len(clave) is 2 and not clave.isdigit():
                bandera = False
        else:
            print ("Ingrese sólo dos letras")
            bandera = True
    abecedario = string.ascii_uppercase
    abecedario_1, abecedario_2 = abecedario.split(clave[1])
    abecedario_clave = clave[1] + abecedario_2 + abecedario_1

    mensaje_separado = mensaje.split()

    for x in mensaje_separado:
        palabra_separada = x

        for y in palabra_separada:
            letra_sin_cifrar = y
            index = abecedario.index(letra_sin_cifrar)
            letra_abc_clave = abecedario_clave[index]
            
            if y is palabra_separada[-1]:
                mensaje_cifrado += letra_abc_clave + ' '
            else:
                mensaje_cifrado += letra_abc_clave

    return '\n Mensaje cifrado: '+mensaje_cifrado

def descifrar_alberti():
    mensaje_descifrado = ''
    bandera = True

    while bandera == True:    
        mensaje = input('¿Cuál es el mensaje que desea descifrar? ').upper()
        if not mensaje.isdigit():
            bandera = False
        else:
            print ("Ingrese sólo letras")
            bandera = True

    bandera = True
    
    while bandera == True:
        clave = input('¿Cuál es la clave que desea utilizó para cifra el mensaje? ').upper()
        if len(clave) is 2 and not clave.isdigit():
                bandera = False
        else:
            print ("Ingrese sólo dos letras")
            bandera = True

    abecedario = string.ascii_uppercase
    abecedario_1, abecedario_2 = abecedario.split(clave[1])
    abecedario_clave = clave[1] + abecedario_2 + abecedario_1
    
    mensaje_separado = mensaje.split()

    for x in mensaje_separado:
        palabra_separada = x

        for y in palabra_separada:
            letra_sin_cifrar = y
            index = abecedario_clave.index(letra_sin_cifrar)
            letra_abc_clave = abecedario[index]
            
            if y is palabra_separada[-1]:
                mensaje_descifrado += letra_abc_clave + ' '
            else:
                mensaje_descifrado += letra_abc_clave

    return '\n Mensaje descifrado: '+mensaje_descifrado

def cifrado_hill(message, key, decrypt = False):
    from math import sqrt
    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Longitud de clave no válida")

    alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-;|'
    tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])

    if len(message) % n > 0:
        message += '|' * (n - (len(message) % n))

    keylist = []
    for a in key:
        keylist.append(tonum[a])

    keymatrix = [] 
    for i in range(n):
        keymatrix.append(keylist[i * n : i * n + n])

    from numpy import matrix
    from numpy import linalg

    keymatrix = matrix(keymatrix).round().T

    if decrypt:
        determinant = linalg.det(keymatrix).round()
        
        if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
        elif determinant % len(alpha) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")

        inverse = []
        keymatrix =  matrix(keymatrix.getI() * determinant).round()

        invdeterminant = 0
        for i in range(10000):
            if (determinant * i % len(alpha)) == 1:
                invdeterminant = i
                break

        for row in keymatrix.getA() * invdeterminant:
            newrow = []
            for i in row:
                newrow.append( i.round() % len(alpha) )
            inverse.append(newrow)
        
        keymatrix = matrix(inverse)

    out = ''
    for i in range(len(message) // n):
        lst = matrix( [[tonum[a]] for a in message[i * n:i * n + n]] )
        result = keymatrix * lst
        out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in range(len(result))])
    
    return out

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




#Inicia menu del programa
cifrar()