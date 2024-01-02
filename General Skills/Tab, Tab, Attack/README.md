# ARMssembly 1
![Descripcion del CTF](img/description.png)

## Descripción
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip)

## Resolución
En este CTF nos dan un archivo .zip. lo descargamos y descomprimimos:

![Consola](img/console1.png)

La estructura de la carpeta es una única subcarpeta, que contiene otra del mismo nombre sucesivamente:

![Consola](img/console2.png)

Al llegar a cierta profundidad, encontraremos un archivo binario con permisos de ejecución:

![Consola](img/console3.png)

Al ejecutarlo nos proporcionará la flag:

![Consola](img/console4.png)

picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}