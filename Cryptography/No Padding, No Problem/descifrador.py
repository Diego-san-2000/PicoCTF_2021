from Crypto.Util.number import *    #lonng_to_bytes
from pwn import *                   #remote()
from decimal import *               #Decimal()
import re                           #search()

getcontext().prec = 1000 #Precisión de Decimal()

conn = remote('mercury.picoctf.net', 30048)
enunciado = conn.recvuntil('Give me ciphertext to decrypt:').decode()

#Obtenemos n, e y c con expresiones regulares
mensaje = re.search(r"n: ([0-9]+)\ne: ([0-9]+)\nciphertext: ([0-9]+)", enunciado)
n = int(mensaje[1])
e = int(mensaje[2])
c = int(mensaje[3])

micifrado = c * pow(2, e, n)

conn.send(str(micifrado) + '\n')

resultado = conn.recvline().decode()

#Buscamos el texto cifrado
mensaje = re.search(r"([0-9]+)", resultado)
resultado = int(Decimal(mensaje[1]) / 2)

print('Result:', long_to_bytes(resultado))