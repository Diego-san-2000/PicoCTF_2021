![Descripcion del CTF](img/description.png)

En este caso, nos dan un archivo compilado llamado ‘source’ al cual le tendremos que dar permisos de ejecución ($ chmod +x source) para poder abrir.

También nos proporcionan un enlace al servidor donde está el programa corriendo.

Al ejecutar el programa nos encontraremos con el siguiente menú:  
![Imagen de source](img/program1.png)
Si introducimos un número negativo, podremos acabar teniendo dinero negativo:  
![Imagen de source](img/program2.png)
Sabiendo que el programa acepta números negativos, si compramos un número negativo de frutas nuestro dinero aumentará (- cantidad * – coste = + dinero):  
![Imagen de source](img/program3.png)
Una vez que descubrimos esto, lo podemos comprobar en el servidor para obtener la flag: 
![Imagen de source](img/program4.png)
Pegamos el resultado en [cybercheff](https://gchq.github.io/CyberChef/) con la opción ‘From Decimal’ y obtenemos la flag:  
![Cybercheff](img/cybercheff.png)