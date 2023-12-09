import kmeans as km
import img
from PIL import Image

df, ancho,altura = img.toRGB('descarga.jpeg')

imgkm = km.kmeans(3,df.values)

clusters_img = imgkm.inicializarCentroides()

dfNew = df.copy()

for i in range(len(df)):
    centroid_values = imgkm.centroides[clusters_img[i]]
    dfNew.at[i, 'R'] = round(centroid_values[0])
    dfNew.at[i, 'G'] = round(centroid_values[1])
    dfNew.at[i, 'B'] = round(centroid_values[2])

# Imprimir la iamgen final
array = dfNew[['R','G','B']].values.reshape((altura,ancho,3)).astype('uint8')
imgfinal = Image.fromarray(array)
imgfinal.show()
