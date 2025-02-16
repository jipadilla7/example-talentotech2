import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


# Generar datos aleatorios
np.random.seed(42)
x = np.linspace(-10, 10, 300)
y1 = np.sin(x) + np.random.normal(0, 0.2, len(x))
y2 = np.cos(x) + np.random.normal(0, 0.2, len(x))
y3 = np.tan(x) / 10 + np.random.normal(0, 0.1, len(x))  # Limitamos la tangente
y4 = norm.pdf(x, loc=0, scale=2) + np.random.normal(0, 0.02, len(x))
y5 = np.exp(-x**2 / 20) + np.random.normal(0, 0.02, len(x))

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'x': x,
    'Seno con ruido': y1,
    'Coseno con ruido': y2,
    'Tangente ajustada': y3,
    'Distribución Normal': y4,
    'Función Gaussiana': y5
})

# Aplicación en Streamlit
st.title("Visualización de Variables Aleatorias")

st.write("Este dashboard muestra cinco variables aleatorias útiles para análisis y visualización.")

# Gráfico interactivo
fig, ax = plt.subplots()
ax.plot(df['x'], df['Seno con ruido'], label="Seno con ruido")
ax.plot(df['x'], df['Coseno con ruido'], label="Coseno con ruido")
ax.plot(df['x'], df['Tangente ajustada'], label="Tangente ajustada")
ax.plot(df['x'], df['Distribución Normal'], label="Distribución Normal")
ax.plot(df['x'], df['Función Gaussiana'], label="Función Gaussiana")

ax.set_xlabel("X")
ax.set_ylabel("Valores")
ax.set_title("Gráfica de variables aleatorias")
ax.legend()

st.pyplot(fig)

# Mostrar los primeros datos en una tabla
st.write("Vista previa de los datos generados:")
st.dataframe(df.head())
