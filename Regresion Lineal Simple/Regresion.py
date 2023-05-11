"""
@author: Santiago
"""
# Regresión lineal simple.

import numpy as np #contiene las herramientas de matematicas necesarias
import matplotlib.pyplot as plt # es la libreria para 'imprimir' los resultados
import pandas as pd #libreria para cargar y manipular los datos

# Importar el DataSet.
dataset = pd.read_csv('Salary_Data.csv') #sintaxis para cargar los datos
X = dataset.iloc[:, :-1].values #vamos a tomar todas las filas y todas las columnas salvo la ultima columna.
y = dataset.iloc[:, 1].values #elegir variable dependiente

# Dividir el data set en conjunto de entrenamiento y de testing.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state=0)

# Crear modelo de Regresion Lineal Simple con el conjunto de entrenamiento.
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predecir el conjunto de test.
y_pred = regression.predict(X_test)

# Visualizar los resultados de entrenamiento.
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()

# Visualizar los datos de test.
plt.scatter(X_test, y_test, color = "green")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()