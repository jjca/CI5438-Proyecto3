import kmeans as km
import img
from PIL import Image
df, ancho,altura = img.toRGB('descarga.jpeg')

imgkm = km.kmeans(3,df.values)
clusters_img = imgkm.inicializarCentroides()
#print(clusters_img.tolist())

print(imgkm.centroides)

# Imprimir la iamgen final
array = df[['R','G','B']].values.reshape((altura,ancho,3)).astype('uint8')
imgfinal = Image.fromarray(array)
imgfinal.show()

#plt.imshow(df.astype(np.uint8))
#plt.show()