import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Perceptron function ---
def perceptron(x1, x2, w1, w2, b):
    z = w1 * x1 + w2 * x2 + b
    return 1 if z >= 0 else 0

# --- Plotting function ---
def plot_dataset(title, dataset, w1, w2, b):
    st.subheader(title)

    # Sliders
    w1 = st.slider(f"{title} - Weight w1", -2.0, 2.0, w1, 0.1)
    w2 = st.slider(f"{title} - Weight w2", -2.0, 2.0, w2, 0.1)
    b  = st.slider(f"{title} - Bias b", -2.0, 2.0, b, 0.1)

    # Evaluate perceptron
    results = []
    for (x1, x2, target) in dataset:
        y = perceptron(x1, x2, w1, w2, b)
        results.append((x1, x2, target, y))

    # Plot
    fig, ax = plt.subplots()
    for (x1, x2, target, y) in results:
        color = "green" if target == 1 else "red"
        marker = "o" if y == target else "x"  # correct vs incorrect
        ax.scatter(x1, x2, c=color, marker=marker, s=200,
           edgecolors="black" if marker == "o" else None)


    # Decision boundary line: w1*x1 + w2*x2 + b = 0
    x_vals = np.linspace(-0.5, 1.5, 100)
    if w2 != 0:
        y_vals = -(w1 * x_vals + b) / w2
        ax.plot(x_vals, y_vals, "b--")

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    st.pyplot(fig)

    # Show truth table comparison
    st.write("Truth table vs perceptron output:")
    for (x1, x2, target, y) in results:
        st.write(f"({x1},{x2}) → target={target}, perceptron={y}")

# --- Datasets ---
AND_data = [(0,0,0),(0,1,0),(1,0,0),(1,1,1)]
OR_data  = [(0,0,0),(0,1,1),(1,0,1),(1,1,1)]
XOR_data = [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]

st.title("Perceptron Demo: AND, OR, XOR")

# Vertical stacking
plot_dataset("AND Perceptron", AND_data, w1=1.0, w2=1.0, b=-1.5)
plot_dataset("OR Perceptron", OR_data, w1=1.0, w2=1.0, b=-0.5)
plot_dataset("XOR Perceptron", XOR_data, w1=1.0, w2=1.0, b=-0.5)
