import numpy as np
from PIL import Image

# Obtenemos imágenes (hay que ejecutar el script en la misma carpeta)
imagen1 = Image.open("scrambled1.png")
imagen2 = Image.open("scrambled2.png")

# Convertimos las imágenes en matrices
array1 = np.array(imagen1)
array2 = np.array(imagen2)

# Sumamos las matrices
array3 = array1 + array2

# Convertimos la matriz a imagen y guardamos
Image.fromarray(array3).save('output.png')