import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generating random data
np.random.seed(42)
x = np.linspace(-10, 10, 300)
y1 = np.sin(x) + np.random.normal(0, 0.2, len(x))
y2 = np.cos(x) + np.random.normal(0, 0.2, len(x))
y3 = np.tan(x) / 10 + np.random.normal(0, 0.1, len(x))  # Limited tangent function
y4 = norm.pdf(x, loc=0, scale=2) + np.random.normal(0, 0.02, len(x))
y5 = np.exp(-x**2 / 20) + np.random.normal(0, 0.02, len(x))

# Creating a DataFrame
df = pd.DataFrame({
    'x': x,
    'Sine with noise': y1,
    'Cosine with noise': y2,
    'Adjusted Tangent': y3,
    'Normal Distribution': y4,
    'Gaussian Function': y5
})

# Streamlit application
st.title("Random Variable Visualization")

st.write("This dashboard displays five randomly generated variables for analysis and visualization.")

# Plot interactive graph
fig, ax = plt.subplots()
ax.plot(df['x'], df['Sine with noise'], label="Sine with noise")
ax.plot(df['x'], df['Cosine with noise'], label="Cosine with noise")
ax.plot(df['x'], df['Adjusted Tangent'], label="Adjusted Tangent")
ax.plot(df['x'], df['Normal Distribution'], label="Normal Distribution")
ax.plot(df['x'], df['Gaussian Function'], label="Gaussian Function")

ax.set_xlabel("X")
ax.set_ylabel("Values")
ax.set_title("Graph of Random Variables")
ax.legend()

st.pyplot(fig)

# Display first few rows in a table
st.write("Preview of Generated Data:")
st.dataframe(df.head())
