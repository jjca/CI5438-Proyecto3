from PIL import Image
import numpy as np
import pandas as pd
# Open the image
def toRGB(ruta):
    imagen = Image.open(ruta).convert("RGB")

    ancho, altura = imagen.size

    pix = np.asarray(imagen.getdata())

    df = pd.DataFrame(pix, columns=['R','G','B'])

    return df,ancho,altura