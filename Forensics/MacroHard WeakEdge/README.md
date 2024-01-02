# Macrohard WeakEdge
![Descripcion del CTF](img/description.png)

## Descripción
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm)

## Resolución
Nos dan un archivo .pptm, de hoja de presentaciones, al abrirlo tiene 58 diapositivas, todas en blanco menos la primera y la 37:

![PowerPoint](img/powerpoint.png)

Exploramos con exiftool y con strings y no encontramos nada. Al extraer con binwalk:

```
binwalk -e Forensics\ is\ fun
```
 
Se nos creará la siguiente carpeta con este contenido:

![Consola](img/console1.png)

Explorando el resultado del binwalk, encontraremos un archivo llamado hidden:

![Carpeta](img/folder.png)

El archivo tendrá el siguiente contenido:

![Consola](img/console2.png)

Introducimos el resultado en [Cyberchef](https://gchq.github.io/CyberChef/):

![Cybercheff](img/cybercheff.png)

Y obtendremos la flag: 'picoCTF{Did_u_kn0w_ppts_r_zip5}'
