import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Cargar el dataset
file_path = "agroindustria.csv"  # Asegúrate de que el archivo esté en la misma carpeta
df = pd.read_csv(file_path)

# Mostrar primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Resumen estadístico
print("\nResumen Estadístico:")
print(df.describe())

# Verificar valores nulos
print("\nValores Nulos por Columna:")
print(df.isnull().sum())

# Matriz de correlación
correlacion = df.corr()

# Gráfico de correlación
plt.figure(figsize=(10,6))
sns.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación entre Variables Numéricas")
plt.show()

# Histogramas de variables clave
df.hist(figsize=(12,8), bins=20, edgecolor='black')
plt.suptitle("Distribución de Variables en el Dataset", fontsize=14)
plt.show()

# Relación entre Uso de Fertilizante y Rendimiento
plt.figure(figsize=(8,6))
sns.scatterplot(x=df["Uso de Fertilizante (kg/Ha)"], y=df["Rendimiento (Ton/Ha)"], alpha=0.7)
plt.xlabel("Uso de Fertilizante (kg/Ha)")
plt.ylabel("Rendimiento (Ton/Ha)")
plt.title("Relación entre Uso de Fertilizante y Rendimiento")
plt.show()

# Cálculo de regresión lineal entre Uso de Fertilizante y Rendimiento
x = df["Uso de Fertilizante (kg/Ha)"]
y = df["Rendimiento (Ton/Ha)"]
slope, intercept, r_value, p_value, std_err = linregress(x, y)

print("\nRegresión Lineal entre Uso de Fertilizante y Rendimiento:")
print(f"Pendiente: {slope:.4f}")
print(f"Intercepto: {intercept:.4f}")
print(f"Coeficiente de correlación (R): {r_value:.4f}")
print(f"Valor P: {p_value:.4e}")

# Visualización de la regresión lineal
plt.figure(figsize=(8,6))
sns.regplot(x=x, y=y, line_kws={"color":"red"})
plt.xlabel("Uso de Fertilizante (kg/Ha)")
plt.ylabel("Rendimiento (Ton/Ha)")
plt.title("Regresión Lineal entre Uso de Fertilizante y Rendimiento")
plt.show()

# Boxplot de margen de beneficio por tipo de cultivo
plt.figure(figsize=(10,6))
sns.boxplot(x=df["Tipo de Cultivo"], y=df["Margen de Beneficio (USD)"], palette="Set2")
plt.xticks(rotation=45)
plt.title("Margen de Beneficio por Tipo de Cultivo")
plt.show()
