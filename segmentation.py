import kmeans as km
import img
from PIL import Image

df, ancho,altura = img.toRGB('img01.jpeg')

k = [2,4,8,16,32,64,128,256]
iter = 200
for i in k:
    imgkm = km.kmeans(i,df.values,iter)

    clusters_img = imgkm.inicializarCentroides()

    dfNew = df.copy()

    for j in range(len(df)):
        centroid_values = imgkm.centroides[clusters_img[j]]
        dfNew.at[j, 'R'] = round(centroid_values[0])
        dfNew.at[j, 'G'] = round(centroid_values[1])
        dfNew.at[j, 'B'] = round(centroid_values[2])

    # Imprimir la iamgen final
    array = dfNew[['R','G','B']].values.reshape((altura,ancho,3)).astype('uint8')
    imgfinal = Image.fromarray(array)
    imgfinal.save('./clustered/'+'gi'+'_k_'+str(i)+'.jpeg')