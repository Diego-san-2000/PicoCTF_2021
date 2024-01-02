# Wireshark doo dooo ddo doo…
![Descripcion del CTF](img/description.png)

## Descripción
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/d6f9aa16d2a2c51d2e431e658d87af9e/shark1.pcapng).

## Resolución
Nos descargamos el archivo y lo abrimos con wireshark:

![Consola](img/console.png)

Parece un intercambio de paquetes entre kerberos y un cliente usando los protocolos TCP y HTTP:

![Wireshark](img/wireshark.png)

Analizando primero la secuencia TCP nos encontramos con 16 secuencias, donde la 5 parece tener un mensaje con formato de flag:

![Wireshark](img/wireshark2.png)

Como tiene caracteres alfabéticos, podemos pensar que es cifrado por un algoritmo de cifrado por rotación, lo llevamos a [cybercheff](https://gchq.github.io/CyberChef/) y probamos los diferentes algoritmos:

![Cybercheff](img/cybercheff.png)

Con ROT13 obtendremos la flag 'picoCTF{p33kab00_1_s33_u_deadbeef}'