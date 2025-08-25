import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reactor Químico Interactivo", layout="centered")

# Título
st.title("📊 Simulación Interactiva de un Reactor Químico de Primer Orden")
st.write("""
Este recurso permite explorar cómo cambia la concentración de un reactivo **A** en un 
**reactor de flujo pistón (PFR)** con una reacción de primer orden.
La ecuación que se resuelve es:

$$ C_A(t) = C_{A0} \cdot e^{-k \cdot t} $$
""")

# Parámetros ajustables
st.sidebar.header("Parámetros del modelo")
CA0 = st.sidebar.slider("Concentración inicial Cₐ₀ (mol/L)", 0.1, 2.0, 1.0, 0.1)
k = st.sidebar.slider("Constante de reacción k (1/s)", 0.01, 1.0, 0.2, 0.01)
t_max = st.sidebar.slider("Tiempo de residencia (s)", 1, 50, 10, 1)

# Datos
t = np.linspace(0, t_max, 200)
CA = CA0 * np.exp(-k * t)

# Gráfica
fig, ax = plt.subplots()
ax.plot(t, CA, label="Cₐ(t)", linewidth=2)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Concentración de A (mol/L)")
ax.set_title("Decaimiento de concentración en un reactor de primer orden")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Resultado clave
st.subheader("Resultado numérico")
st.write(f"A la salida del reactor (t = {t_max} s):")
st.latex(f"C_A = {CA[-1]:.3f} \, mol/L")
