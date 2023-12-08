import numpy as np
import matplotlib.pyplot as plt

"""
Clase kmeans
Se inicializa con el valor k de la cantidad de clusters
Y el conjunto de datos X
"""
class kmeans:
    def __init__(self, k, X) -> None:
        self.k = k
        self.centroides = None
        self.iteraciones = 200
        self.datos = X
    
    """
    Funcion que recibe el arreglo de Xs y retorna los centroides inicializados
    El calculo se realiza usando librerías de numpy para obtener los valores dentro del rango de los datos
    usando una distribución uniforme.
    En uniform hay 3 args
    np.amin: Por cada dimensión en X, se obtiene el mínimo.
    np.amax: por cada dimensión en X, se obtiene el máximo.
    size es la cantidad de centroides (k) 
    """
    def inicializarCentroides(self):
        self.centroides = np.random.uniform(np.amin(self.datos, axis=0), np.amax(self.datos,axis=0),size=(self.k,self.datos.shape[1]))
        for _ in range(self.iteraciones):
            Y = []
            # Cálculo de las distancias euclidenanas
            for punto in self.datos:
                distancias = self.distanciaEuclideana(punto) # lista de distancias entre el punto y cada centroide
                numero_cluster = np.argmin(distancias) # asigna el punto al cluster de acuerdo al centroide
                Y.append(numero_cluster) # lo guarda en la lista
            
            Y = np.array(Y)

            cluster_index = [] # 
            for j in range(self.k):
                cluster_index.append(np.argwhere(Y == j))

            cluster_centro = [] # Mitad de los clusters
            
            # Calcula la nueva ubicación del centroide usando la media

            for j, indice in enumerate(cluster_index):
                if len(indice) == 0:
                    cluster_centro.append(self.centroides[j])
                else: 
                    cluster_centro.append(np.mean(self.datos[indice],axis = 0 )[0])
                

            # Condicion de parada de que lso clusters no se han movido y no hacer más iteraciones
            if np.max(self.centroides - np.array(cluster_centro)) < 0.0001:
                break
            else:
                self.centroides = np.array(cluster_centro)
        return Y

    def distanciaEuclideana(self,puntos):
        return np.sqrt(np.sum((self.centroides - puntos)**2, axis =1 ))
    
