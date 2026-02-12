"""
Demo interactiva de Perceptrón
Visualización de operaciones lógicas AND, OR y XOR usando perceptrones simples
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def perceptron(x1, x2, w1, w2, b):
    """
    Función de perceptrón simple
    
    Args:
        x1: Primera entrada
        x2: Segunda entrada
        w1: Peso de la primera entrada
        w2: Peso de la segunda entrada
        b: Bias (sesgo)
    
    Returns:
        1 si la suma ponderada es >= 0, sino 0
    """
    suma = w1 * x1 + w2 * x2 + b
    return 1 if suma >= 0 else 0

def plot_decision_boundary(w1, w2, b, operation_name):
    """
    Visualiza la frontera de decisión del perceptrón
    
    Args:
        w1: Peso de x1
        w2: Peso de x2
        b: Bias
        operation_name: Nombre de la operación (para el título)
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Crear una malla para visualizar la región de decisión
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    
    # Calcular la salida del perceptrón para cada punto
    Z = np.array([[perceptron(x, y_val, w1, w2, b) for x, y_val in zip(x_row, y_row)] 
                  for x_row, y_row in zip(xx, yy)])
    
    # Visualizar las regiones
    ax.contourf(xx, yy, Z, alpha=0.3, levels=[-0.5, 0.5, 1.5], colors=['lightblue', 'lightcoral'])
    
    # Dibujar la línea de decisión: w1*x1 + w2*x2 + b = 0
    if w2 != 0:
        x_line = np.array([x_min, x_max])
        y_line = -(w1 * x_line + b) / w2
        ax.plot(x_line, y_line, 'k-', linewidth=2, label='Frontera de decisión')
    
    # Plotear los puntos de la tabla de verdad
    points = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for x1, x2 in points:
        output = perceptron(x1, x2, w1, w2, b)
        color = 'red' if output == 1 else 'blue'
        marker = 'o' if output == 1 else 'x'
        ax.scatter(x1, x2, c=color, marker=marker, s=200, edgecolors='black', linewidths=2)
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel('x1', fontsize=14)
    ax.set_ylabel('x2', fontsize=14)
    ax.set_title(f'Frontera de decisión - {operation_name}', fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return fig

def main():
    st.set_page_config(page_title="Demo de Perceptrón", layout="wide")
    
    st.title("🧠 Demo Interactiva de Perceptrón")
    st.markdown("""
    Esta aplicación demuestra cómo funciona un **perceptrón simple**, la unidad básica de las redes neuronales.
    Explora las operaciones lógicas AND, OR y XOR y ajusta los parámetros para ver cómo cambia la frontera de decisión.
    """)
    
    # Selector de operación
    operation = st.sidebar.selectbox(
        "Selecciona una operación lógica:",
        ["AND", "OR", "XOR"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚙️ Ajusta los parámetros")
    
    # Valores iniciales según la operación
    if operation == "AND":
        default_w1, default_w2, default_b = 1.0, 1.0, -1.5
    elif operation == "OR":
        default_w1, default_w2, default_b = 1.0, 1.0, -0.5
    else:  # XOR
        default_w1, default_w2, default_b = 1.0, 1.0, -0.5
    
    # Sliders para ajustar pesos y bias
    w1 = st.sidebar.slider("Peso w1:", -5.0, 5.0, default_w1, 0.1)
    w2 = st.sidebar.slider("Peso w2:", -5.0, 5.0, default_w2, 0.1)
    b = st.sidebar.slider("Bias (b):", -5.0, 5.0, default_b, 0.1)
    
    # Mostrar la ecuación del perceptrón
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📐 Ecuación del perceptrón")
    st.sidebar.latex(f"y = \\begin{{cases}} 1 & \\text{{si }} {w1:.2f}x_1 + {w2:.2f}x_2 + {b:.2f} \\geq 0 \\\\ 0 & \\text{{en otro caso}} \\end{{cases}}")
    
    # Información sobre la operación seleccionada
    st.markdown(f"## Operación: {operation}")
    
    if operation == "AND":
        st.info("""
        **Operación AND**: Devuelve 1 solo cuando **ambas** entradas son 1.
        Esta operación es **linealmente separable** y puede ser resuelta por un perceptrón simple.
        """)
    elif operation == "OR":
        st.info("""
        **Operación OR**: Devuelve 1 cuando **al menos una** entrada es 1.
        Esta operación es **linealmente separable** y puede ser resuelta por un perceptrón simple.
        """)
    else:  # XOR
        st.warning("""
        **Operación XOR**: Devuelve 1 cuando las entradas son **diferentes**.
        Esta operación **NO es linealmente separable** y no puede ser resuelta por un perceptrón simple.
        Se necesita una red neuronal multicapa (al menos 1 capa oculta).
        """)
    
    # Crear dos columnas
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Tabla de verdad")
        
        # Calcular las salidas del perceptrón
        results = []
        expected = {
            "AND": [0, 0, 0, 1],
            "OR": [0, 1, 1, 1],
            "XOR": [0, 1, 1, 0]
        }
        
        for i, (x1_val, x2_val) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
            output = perceptron(x1_val, x2_val, w1, w2, b)
            expected_output = expected[operation][i]
            correct = "✅" if output == expected_output else "❌"
            results.append({
                "x1": x1_val,
                "x2": x2_val,
                f"{operation} esperado": expected_output,
                "Perceptrón": output,
                "Correcto": correct
            })
        
        st.dataframe(results, use_container_width=True)
        
        # Calcular precisión
        correct_count = sum(1 for r in results if r["Correcto"] == "✅")
        accuracy = (correct_count / len(results)) * 100
        st.metric("Precisión", f"{accuracy:.0f}%")
    
    with col2:
        st.markdown("### 🎯 Frontera de decisión")
        fig = plot_decision_boundary(w1, w2, b, operation)
        st.pyplot(fig)
        plt.close()
    
    # Sección educativa
    st.markdown("---")
    st.markdown("## 📚 ¿Qué es un perceptrón?")
    
    st.markdown("""
    Un **perceptrón** es la unidad más básica de una red neuronal artificial. Fue inventado por Frank Rosenblatt en 1957.
    
    ### Funcionamiento:
    1. **Entradas**: Recibe múltiples valores de entrada (x1, x2, ..., xn)
    2. **Pesos**: Cada entrada se multiplica por un peso (w1, w2, ..., wn)
    3. **Suma ponderada**: Se suma todo junto más un bias: `suma = w1*x1 + w2*x2 + ... + b`
    4. **Función de activación**: Si la suma es ≥ 0, la salida es 1; sino, es 0
    
    ### Limitaciones:
    - Solo puede resolver problemas **linealmente separables**
    - No puede resolver XOR con un solo perceptrón
    - Para problemas más complejos se necesitan redes neuronales multicapa
    
    ### ¿Por qué XOR no es linealmente separable?
    Para que un problema sea linealmente separable, debe existir una **línea recta** (en 2D) que separe
    las clases. En el caso de XOR:
    - Los puntos (0,0) y (1,1) deben estar en una región (salida 0)
    - Los puntos (0,1) y (1,0) deben estar en otra región (salida 1)
    
    No hay forma de trazar una sola línea recta que separe estos puntos correctamente. Se necesitarían
    al menos dos líneas, lo que requiere una red neuronal con capas ocultas.
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Desarrollado con ❤️ usando Streamlit | Proyecto educativo sobre redes neuronales</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
