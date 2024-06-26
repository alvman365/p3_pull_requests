# 1 Definición del problema de negocio
# ¿Cómo puedo definir un problema de negocio?
# ¿Cuáles son los problemas de negocio que típicamente con resueltos con Data Science?
############################################
# Carlos Olid. Pegar tu enlace aqui:  

############################################
#################################
# Ederson Quintero: Pegar tu enlace aquí: 

#################################
#################################
# Angélica Ríos: Pegar tu enlace aquí: 

#################################

# 2 Objetivos del negocio



# 3 Objetivos de Machine Learning




# 4 Importamos las librerías necesarias

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#5 Ingesta de datos
# ¿En que consiste la ingesta de Datos?
# ¿Qué tecnologias suelen ser mas utlizadas para hacer ingesta de Datos en particular... 
# para un proyecto de Data Science?
df = pd.read_csv("[ruta_al_archivo.csv]")
########################################
# Nathaly Freire. Pegar tu enlace aquí

########################################
# Ignacio Amores. Pegar tu enlace aqui:

########################################


#6 Limpieza de datos
# ¿En qué consiste la limpieza de datos en Data Science y por qué es tan crucial esta etapa?
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["variable_numerica"] = df["variable_numerica"].astype("float")
#################################
# Alvaro Manzanas: Pegar tu enlace aquí: https://github.com/alvman365/p2-modulo3/blob/main/archivos/limpieza%20de%20datos%20alvaro%20manzanas.pdf 

#################################
#################################
# Reinaldo Díaz. Pegar tu enlace aqui:

#################################
#################################
# Ederson Quintero: Pegar tu enlace aquí: 

#################################
#################################
# Luis Torres: Pegar tu enlace aquí: 

#################################



#7 Análisis exploratorio de datos
# ¿Cuál es la importancia de realizar un buen Análisis exploratorio de datos en Data Science?
print(df.describe())
df.hist()
plt.show()
df.corr()
##################################################
# Pedro Álvarez: Pegar tu enlace aqui:

##################################################
##################################################
# Reinaldo Díaz. Pegar tu enlace aquí:

##################################################
#################################
# Angélica Ríos: Pegar tu enlace aquí: 

#################################
#################################
# Luis Torres: Pegar tu enlace aquí: 

#################################



#8 Selección de características (Feature Engineering)
# ¿En qué consiste la selección de caracteristicas de un modelo de machine learning?
X = df[["variable_1", "variable_2"]]
y = df["variable_objetivo"]
###########################################
# Eva Bernal: Pegar tu enlace aqui: 

###########################################
#################################
# Manuel Murillo: Pegar tu enlace aquí: 

#################################
#################################
# Humberto Sánchez: Pegar tu enlace aquí: 

#################################



#9 División de conjuntos de datos
# ¿En que consiste la etapa de Division de conjuntos de Datos?
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)



#10 Entrenamiento del modelo
# ¿En qué consiste la etapa de entrenamiento de un modelo de machine learning?
modelo = LinearRegression()
modelo.fit(X_train, y_train)
####################################################
# Olga Gabrik. Pegar tu enlace aqui:

####################################################
#################################
# Manuel Murillo: Pegar tu enlace aquí: 

#################################
########################################
# Nathaly Freire. Pegar tu enlace aquí

########################################
#######################################
# Irene Serrano. Pegar tu enlace aquí:

#######################################


#11 Evaluación del modelo
# ¿Qué son las métricas de rendimiento de un modelo de Machine Learning?
score_train = modelo.score(X_train, y_train)
score_test = modelo.score(X_test, y_test)
print("Precisión en entrenamiento:", score_train)
print("Precisión en prueba:", score_test)
#######################################################
# Eva Bernal. Pegar tu enlace aqui:

#######################################################
#######################################################
# Olga Gabrik.Pegar tu enlace aquí:

#######################################################
#################################
# Humberto Sánchez: Pegar tu enlace aquí: 

#################################
#######################################
# Irene Serrano. Pegar tu enlace aquí:

#######################################

#12 Predicciones
# ¿En que consiste la etapa de predicciones en un proyecto de Machine Learning?
predicciones = modelo.predict(X_test)


#13 Visualización de resultados
# ¿En qué consiste la etapa de visualización de resultados en un proyecto de Machine Learning?
# ¿Cuáles son las recomendaciones mas importantes según tu experiencia para... 
# hacer una buena visualización de resultados?
plt.scatter(y_test, predicciones)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r")
plt.show()

#######################################
# Ignacio Saura. Pegar tu enlace aquí:

#######################################
# Patricia Garcia: Pegar tu enlace aquí:

######################################
#######################################
# Irene Serrano. Pegar tu enlace aquí:

#######################################


# 14 Deployment del modelo
# ¿Cómo se hace el deployment de un modelo de Machine Learning?
# (Guarde el modelo entrenado para su uso futuro)
import pickle
pickle.dump(modelo, open("modelo.pkl", "wb"))
#########################################################################
# Juan D. Pegar el enlace aquí: 

#########################################################################
#################################
# Alvaro Manzanas: Pegar tu enlace aquí: 

#################################
# 15 (Implemente el modelo en una aplicación web o API)
# ¿Cómo se implementa un modelo de machine learning en una aplicación web o API?
# (Esta parte depende de la plataforma de deployment que se elija)


#########################################################################
# Juan D. Pegar el enlace aquí: 

#########################################################################


#16  Conclusiones
# (Explique los resultados del proyecto y su impacto en el problema de negocio)
# Investigar cómo presentar resultados de proyecto de Ciencia de datos que impacte al publico



