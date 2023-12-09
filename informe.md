# Informe - Proyecto 3 

## Parte 1 - Implementación del algoritmo de K-Means

Se realizó la implementación usando las librerías de `numpy` y siguiendo el esquema sugerido por NeuralNine en su canal https://www.youtube.com/watch?v=5w5iUbTlpMQ.

## Parte 2 - Análisis del Iris Dataset

El objetivo de este análisis es observar si el algoritmo de k-means realiza una clasificación correcta de las plantas basándose en los parámetros dados en el dataset.

Se tienen los siguientes parámetros para realizar una clasificación:

- Ancho del pétalo
- Largo del pétalo
- Largo del sépalo
- Ancho del sépalo

## Parte 3 - Segmentación de Imágenes

Aprovechando las facilidades de los K-means, es posible segmentar las imágenes en `k` colores. Esta herramienta puede ser usada en la compresión de imágenes, al eliminar la cantidad de colores que posee.

Se seleccionaron dos imágenes las cuales se muestran en sus originales a continuación:

|!['Alo'](descarga.jpeg)|<img src="img03.jpeg" style="width:250px">

A fin de tener una comparativa visual se usaron los valores de $k=[2,4,8,16,32,64,128,256]$.

Se tienen las siguientes imágenes para la primera imagen:

|2|4|8|16|
--|--|--|--|
![2](clustered/a380_k_2.png)|![4](clustered/a380_k_4.png)|![8](clustered/a380_k_8.png)|![16](clustered/a380_k_16.png)|

|32|64|128|256|
--|--|--|--|
![32](clustered/a380_k_32.png)|![64](clustered/a380_k_64.png)|![128](clustered/a380_k_128.png)|![256](clustered/a380_k_256.png)|


Para la segunda imagen se obtuvieron las siguientes imágenes:

|2|4|8|16|
--|--|--|--|

|32|64|128|256|
--|--|--|--|
