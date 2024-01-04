from pwn import *
import string

conn = remote("mercury.picoctf.net", 50899)

def enviar(input):
    conn.recvuntil("encrypted:")
    conn.sendline(input)
    conn.recvline()
    conn.recvline()
    return int(conn.recvline().decode())

flag = "picoCTF{sheriff_you_solved"
longitud = enviar(flag)
actual = ""
while actual != "}":
    for c in string.printable:
        if enviar(flag + c) <= longitud:
            flag +=c
            actual = c
            print("Construyendo flag: {}".format(flag))
            break
print("La flag es: {}".format(flag))
