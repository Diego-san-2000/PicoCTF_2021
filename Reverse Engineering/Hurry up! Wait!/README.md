# Hurry up! Wait!
![Descripcion del CTF](img/description.png)

## Descripción
[svchost.exe](https://mercury.picoctf.net/static/af4d1c8dce72f8f7b55350f16ab8e3a2/svchost.exe)

## Resolucion
Descargamos el programa, creamos un nuevo proyecto con ghidra y lo analizamos:

![Ghidra](img/ghidra1.png)

Esta es la función que más interesante parece:

![Ghidra](img/ghidra2.png)

Si examinamos la primera llamada, vemos que inprime por pantalla una p:

![Ghidra](img/ghidra3.png)

Vemos que la segunda llamada imprime por pantalla una i, como el inicio de una flag:

![Ghidra](img/ghidra4.png)

Si anotamos la salida de todas las funciones obtendremos la flag: 'picoCTF{d15a5m_ftw_eab78e4}'.