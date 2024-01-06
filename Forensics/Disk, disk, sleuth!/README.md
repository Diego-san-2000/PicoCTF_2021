# Disk, disk, sleuth!
![Descripcion del CTF](img/description.png)

## Descripción
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/4f3df7052b4121aff89af1a3f517afb1/dds1-alpine.flag.img.gz)

## Resolucion
Nos proporcionan una imagen comprimida, por lo que la descomprimimos primero:

```
gunzip dds1-alpine.flag.img.gz
```

La descripción nos dice que usemos 'srch_strings' para encontrar la flag, este comando es igual que 'strings', nos permite encontrar cadenas de caracteres en programas.

Podremos usar cualquiera de los siguientes comandos:

```
srch_strings dds1-alpine.flag.img | grep 'picoCTF{'
```


```
strings dds1-alpine.flag.img | grep 'picoCTF{'
```

Estos comandos se encargan de lo siguiente:
1. "strings dss1-alpine.flag.img" busca todas las cadenas de caracteres en el programa.
2. "|" Pasa la salida del comando anterior como entrada al siguiente comando, es decir, todos los resultados obtenidos los analizará el siguiente comando.
3. "grep 'picoCTF{'" imprime por pantalla todas las coincidencias que se den con la cadena proporcionada.

![Consola](img/console.png)

Obteniendo así la flag 'picoCTF{f0r3ns1c4t0r_n30phyt3_a011c142}'.