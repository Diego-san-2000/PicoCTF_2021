# Shop writeup

![Descripcion del CTF](img/description.png)  

## Descripción

Best Stuff - Cheap Stuff, Buy Buy Buy... Store instance: [source](https://mercury.picoctf.net/static/a94b408ab46e6bd72f915d68be8aebc0/source). The shop is open for business at nc mercury.picoctf.net 42159.

## Resolución
En este caso, nos dan un archivo compilado llamado ‘source’ al cual le tendremos que dar permisos de ejecución para poder abrir.

`chmod +x source` bash

También nos proporcionan un enlace al servidor donde está el programa corriendo.

Al ejecutar el programa nos encontraremos con el siguiente menú:

![Imagen de source](img/program1.png)

Si introducimos un número negativo, podremos acabar teniendo dinero negativo:

![Imagen de source](img/program2.png)

Sabiendo que el programa acepta números negativos, si compramos un número negativo de frutas nuestro dinero aumentará (- cantidad * – coste = + dinero):

![Imagen de source](img/program3.png)

Una vez que descubrimos esto, lo podemos comprobar en el servidor para obtener la flag:

![Imagen de source](img/program4.png)

Pegamos el resultado en [Cybercheff](https://gchq.github.io/CyberChef/) con la opción ‘From Decimal’ y obtenemos la flag:

![Cybercheff](img/cybercheff.png)