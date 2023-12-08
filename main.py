import pandas as pd
import kmeans
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

df = pd.read_csv('./iris.csv')

#sns.FacetGrid(df,hue="species",height=3).map(sns.histplot,"petal_length",stat="density").add_legend()

#sns.set_style("whitegrid")
#sns.pairplot(df,hue="species",size=3)

sns.FacetGrid(df,hue="species",height=6).map(plt.scatter_3d,"petal_length","petal_width").add_legend()

#plt.scatter(iris_setosa['petal_length'], iris_setosa['petal_width'])
plt.show()

""" df.drop(columns=['species'],axis = 1,inplace=True)
df.drop(columns=['sepal_length'],axis = 1, inplace=True)
df.drop(columns=['sepal_width'],axis = 1, inplace=True)
kmean = kmeans.kmeans(3 ,df.values)
Y = kmean.inicializarCentroides()

plt.scatter(df['petal_length'], df['petal_width'], c=Y)
plt.scatter(kmean.centroides[:,0], kmean.centroides[:,1],c = range(len(kmean.centroides)),marker="*",s = 200)
plt.show() """