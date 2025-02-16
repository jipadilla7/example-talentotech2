import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Configuración de la aplicación
st.title("📊 Análisis de Datos Agroindustriales")
st.markdown("Este dashboard interactivo permite analizar los datos de agroindustria con diferentes visualizaciones.")

# Cargar el dataset
file_path = "agroindustria.csv"  # Asegúrate de que el archivo esté en la misma carpeta
df = pd.read_csv(file_path)

# Mostrar primeras filas
st.subheader("📌 Vista previa de los datos")
st.dataframe(df.head())

# Resumen estadístico
st.subheader("📊 Estadísticas descriptivas")
st.write(df.describe())

# Verificar valores nulos
st.subheader("❗ Valores nulos en el dataset")
st.write(df.isnull().sum())

# Filtrar solo las columnas numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Matriz de correlación
st.subheader("📈 Matriz de Correlación")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)



# Histograma de variables clave
st.subheader("📊 Distribución de Variables")
fig, ax = plt.subplots(figsize=(12, 8))
df.hist(ax=ax, bins=20, edgecolor='black')
plt.suptitle("Distribución de Variables", fontsize=14)
st.pyplot(fig)

# Relación entre Uso de Fertilizante y Rendimiento
st.subheader("🌾 Relación entre Uso de Fertilizante y Rendimiento")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x=df["Uso de Fertilizante (kg/Ha)"], y=df["Rendimiento (Ton/Ha)"], alpha=0.7, ax=ax)
plt.xlabel("Uso de Fertilizante (kg/Ha)")
plt.ylabel("Rendimiento (Ton/Ha)")
plt.title("Relación entre Uso de Fertilizante y Rendimiento")
st.pyplot(fig)

# Cálculo de regresión lineal
x = df["Uso de Fertilizante (kg/Ha)"]
y = df["Rendimiento (Ton/Ha)"]
slope, intercept, r_value, p_value, std_err = linregress(x, y)

st.subheader("📊 Regresión Lineal entre Uso de Fertilizante y Rendimiento")
st.write(f"**Pendiente:** {slope:.4f}")
st.write(f"**Intercepto:** {intercept:.4f}")
st.write(f"**Coeficiente de correlación (R):** {r_value:.4f}")
st.write(f"**Valor P:** {p_value:.4e}")

# Visualización de la regresión lineal
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(x=x, y=y, line_kws={"color": "red"}, ax=ax)
plt.xlabel("Uso de Fertilizante (kg/Ha)")
plt.ylabel("Rendimiento (Ton/Ha)")
plt.title("Regresión Lineal entre Uso de Fertilizante y Rendimiento")
st.pyplot(fig)

# Boxplot de margen de beneficio por tipo de cultivo
st.subheader("💰 Margen de Beneficio por Tipo de Cultivo")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x=df["Tipo de Cultivo"], y=df["Margen de Beneficio (USD)"], palette="Set2", ax=ax)
plt.xticks(rotation=45)
plt.title("Margen de Beneficio por Tipo de Cultivo")
st.pyplot(fig)

st.subheader("📈 Líneas de Tendencia para Variables Numéricas")

# Seleccionar solo las columnas numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Verificar si hay columnas numéricas
if df_numeric.shape[1] > 1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Iterar sobre cada columna numérica y trazar la línea de tendencia
    colors = plt.cm.get_cmap('tab10', len(df_numeric.columns))  # Paleta de colores automática
    for idx, col in enumerate(df_numeric.columns):
        x = np.arange(len(df_numeric))  # Crear eje X basado en el índice de la DataFrame
        y = df_numeric[col].values
        
        # Ajustar una recta de tendencia
        slope, intercept = np.polyfit(x, y, 1)
        trend_line = slope * x + intercept
        
        # Graficar la línea original y la línea de tendencia
        ax.plot(x, y, label=col, linestyle='dotted', alpha=0.7, color=colors(idx))
        ax.plot(x, trend_line, linestyle='solid', color=colors(idx), label=f"Tendencia {col}")

    ax.set_title("Líneas de Tendencia para Variables Numéricas")
    ax.set_xlabel("Índice de Muestra")
    ax.set_ylabel("Valor")
    ax.legend()
    st.pyplot(fig)

else:
    st.warning("No hay suficientes columnas numéricas para graficar líneas de tendencia.")

