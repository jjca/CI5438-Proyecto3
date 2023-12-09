import pandas as pd
import kmeans
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

df = pd.read_csv('./iris.csv')

#sns.FacetGrid(df,hue="species",height=3).map(sns.histplot,"petal_length",stat="density").add_legend()

#sns.set_style("whitegrid")
#sns.pairplot(df,hue="species",height=3)
#plt.show()

perms = ['sepal_length','sepal_width','petal_width','petal_length']

df.drop(columns=['species'],axis = 1,inplace=True)

print(df.head())
k = 2
""" for i in perms:
    perms_i = perms
    cp = [(i,b) for b in perms_i]
    print(cp)
    for j in cp:
        if j[0] == j[1]:
            pass
        else:
            dfCopy = df.copy()
            dfCopy.drop(dfCopy.columns.difference([j[0],j[1]]),axis = 1, inplace=True)
            print(dfCopy.head())           
            kmean = kmeans.kmeans(k,dfCopy.values,200)  
            Y = kmean.inicializarCentroides()
            dfCopy['centroides'] = kmean.inicializarCentroides()
            plt.scatter(dfCopy[j[0]], dfCopy[j[1]], c=Y)
            plt.xlabel(j[0])
            plt.ylabel(j[1])
            plt.scatter(kmean.centroides[:,0], kmean.centroides[:,1],c ='black',marker="*",s = 100)
            plt.savefig('./plants/'+j[0]+j[1]+'_k'+str(k)+'.png')
            plt.close() """


df.drop(columns=['petal_length'],axis = 1, inplace=True)
df.drop(columns=['petal_width'],axis = 1, inplace=True)
kmean = kmeans.kmeans(k,df.values,200)  
Y = kmean.inicializarCentroides()
plt.scatter(df['sepal_width'], df['sepal_length'], c=Y)
plt.scatter(kmean.centroides[:,0], kmean.centroides[:,1],c ='black',marker="*",s = 100)
plt.show()
