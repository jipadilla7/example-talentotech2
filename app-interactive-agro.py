import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la aplicación
st.title("📊 Dashboard Interactivo de Agroindustria")
st.markdown("Explora los datos de agroindustria con gráficos interactivos y filtros dinámicos.")

# Cargar el dataset
file_path = "agroindustria.csv"  # Asegúrate de que el archivo esté en la misma carpeta
df = pd.read_csv(file_path)

# Seleccionar columnas categóricas y numéricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

# Permitir al usuario seleccionar la variable categórica y numérica
st.sidebar.header("📌 Selección de Datos")
x_axis = st.sidebar.selectbox("Selecciona una Variable Categórica", categorical_cols)
y_axis = st.sidebar.selectbox("Selecciona una Variable Numérica", numerical_cols)

# Filtrar datos por región (ejemplo)
region_filter = st.sidebar.multiselect("Filtrar por Región", df["Región"].unique(), default=df["Región"].unique())

# Aplicar filtro
filtered_df = df[df["Región"].isin(region_filter)]

# Gráfico de Barras Interactivo
st.subheader(f"📊 Gráfico de Barras: {y_axis} por {x_axis}")
fig = px.bar(filtered_df, x=x_axis, y=y_axis, color=x_axis, barmode="group", title=f"{y_axis} por {x_axis}")
st.plotly_chart(fig, use_container_width=True)

# Mostrar datos filtrados
st.subheader("📄 Datos Filtrados")
st.dataframe(filtered_df)

# Gráfico Comparativo entre Variables Numéricas
st.subheader("📈 Comparación entre Variables Numéricas")
var_x = st.selectbox("Selecciona el Eje X", numerical_cols)
var_y = st.selectbox("Selecciona el Eje Y", numerical_cols)

fig2 = px.scatter(df, x=var_x, y=var_y, color=df[x_axis], title=f"Relación entre {var_x} y {var_y}")
st.plotly_chart(fig2, use_container_width=True)
