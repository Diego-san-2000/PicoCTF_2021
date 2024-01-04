import binascii
from Crypto.Cipher import DES
from tqdm import tqdm

#pad copiado de ddes.py
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def combinatoriaDES(descripcion, input, encrypt):
    diccionario = {}
    for key in tqdm(range(MAXCOMBINACION), desc=descripcion):
        key = (f"{key:06}" + padding).encode()                                  #Modificcamos la calve para que tenga el padding necesario
        cipher = DES.new(key, DES.MODE_ECB)
        result = cipher.encrypt(input) if encrypt else cipher.decrypt(input)    #Calculamos el resultado con la clave según se cifre o descifre
        diccionario[result] = key                                               #Guardamos el par resultado-clave en el diccionario
    return diccionario

padding = "  "
flag = binascii.unhexlify("6f745ccee635f76746be185541b9f9c046b8d707f93d0522e2325fb041c59ec7bbbaa818d7c51381")
#Convertimos a bytes y saneamos el input con el pad
inputBytes = pad(binascii.unhexlify("13371337").decode())
cifradoBytes = binascii.unhexlify("8f45ca8a9264c2aa")
MAXCOMBINACION = 999999

#Calculamos posibles claves
diccionarioCifrado = combinatoriaDES("Calculando cifrados", inputBytes, True)
diccionarioDescifrado = combinatoriaDES("Calculando descifrados", cifradoBytes, False)

'''
Cambiamos a set para tener complejidad O(1) con la intersección.
Aunque se use keys(), se están comparando los cifrados con los descifrados,
solo que se llaman keys por ser la clave del diccionario
'''
conjunto = set(diccionarioCifrado.keys()) & set(diccionarioDescifrado.keys())

#Obtenemos la coincidencia y las claves del cifrado y descifrado de los diccionarios
cifradoIdentico = conjunto.pop()
primeraKey = diccionarioCifrado[cifradoIdentico]
segundaKey = diccionarioDescifrado[cifradoIdentico]

print("Clave 1: {}".format(primeraKey))
print("Clave 2: {}".format(segundaKey))

#Creamos los objetos DES para descifrar la flag
cifrado1 = DES.new(primeraKey, DES.MODE_ECB)
cifrado2 = DES.new(segundaKey, DES.MODE_ECB)

flagDescifrada = cifrado1.decrypt(cifrado2.decrypt(flag)).decode()
print("Flag: {}".format(flagDescifrada))