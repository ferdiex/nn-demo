# 🧠 Perceptrón Demo - Neural Network Basics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Una demostración interactiva de perceptrones para entender los fundamentos de las redes neuronales. Visualiza cómo un perceptrón simple puede aprender operaciones lógicas como AND, OR y por qué no puede resolver XOR.

## 🎯 Descripción

Este proyecto es una herramienta educativa que te permite experimentar con perceptrones de forma visual e interactiva. Utiliza Streamlit para crear una interfaz donde puedes ajustar los pesos y el sesgo (bias) de un perceptrón y ver en tiempo real cómo afecta la clasificación de puntos.

### ¿Qué es un Perceptrón?

Un perceptrón es la unidad básica de una red neuronal. Toma múltiples entradas, las multiplica por pesos, suma un sesgo y produce una salida binaria basándose en una función de activación.

**Fórmula:**
```
z = w1*x1 + w2*x2 + b
y = 1 si z >= 0, sino 0
```

## ✨ Características

- 📊 **Visualización interactiva**: Gráficos en tiempo real de la clasificación
- 🎛️ **Control manual**: Ajusta pesos (w1, w2) y sesgo (b) con sliders
- 📈 **Frontera de decisión**: Visualiza la línea que separa las clases
- ✅ **Validación instantánea**: Compara la salida con la tabla de verdad esperada
- 🔴🟢 **Código de colores**: Verde para clase 1, rojo para clase 0
- ⭕❌ **Indicadores de precisión**: Círculos para clasificaciones correctas, cruces para incorrectas

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clona el repositorio**
```bash
git clone https://github.com/ferdiex/nn-demo.git
cd nn-demo
```

2. **Crea un entorno virtual (recomendado)**
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

## 💻 Uso

Ejecuta la aplicación con Streamlit:

```bash
streamlit run nn_demo.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🎮 Cómo Usar la Demo

1. **Experimenta con los sliders**: Ajusta los valores de w1, w2 y b para cada operación lógica
2. **Observa la frontera de decisión**: La línea azul discontinua muestra cómo el perceptrón divide el espacio
3. **Verifica la precisión**: 
   - ⭕ Círculos = clasificación correcta
   - ❌ Cruces = clasificación incorrecta
4. **Lee la tabla de verdad**: Compara la salida esperada vs. la salida del perceptrón

## 📚 Operaciones Lógicas

### AND (Y lógico)
- **Linealmente separable**: ✅ Sí
- **Pesos sugeridos**: w1=1.0, w2=1.0, b=-1.5
- Salida 1 solo cuando ambas entradas son 1

### OR (O lógico)
- **Linealmente separable**: ✅ Sí
- **Pesos sugeridos**: w1=1.0, w2=1.0, b=-0.5
- Salida 1 cuando al menos una entrada es 1

### XOR (O exclusivo)
- **Linealmente separable**: ❌ No
- **Demostración**: No importa cómo ajustes los pesos, ¡no podrás clasificar correctamente todos los puntos!
- Este es un problema histórico importante que llevó al desarrollo de redes neuronales multicapa

## 🧪 Conceptos Técnicos

### Separabilidad Lineal

Un conjunto de datos es **linealmente separable** si puedes trazar una línea recta (en 2D) o un hiperplano (en dimensiones superiores) que separe perfectamente las dos clases.

- ✅ **AND y OR**: Son linealmente separables, un perceptrón simple puede aprenderlos
- ❌ **XOR**: No es linealmente separable, requiere una red neuronal con capas ocultas (MLP)

### Frontera de Decisión

La ecuación de la línea de decisión es:
```
w1*x1 + w2*x2 + b = 0
```

Despejando x2:
```
x2 = -(w1*x1 + b) / w2
```

Esta línea divide el espacio en dos regiones donde el perceptrón predice 0 o 1.

## 📁 Estructura del Proyecto

```
nn-demo/
├── nn_demo.py          # Aplicación principal
├── requirements.txt    # Dependencias
├── README.md          # Este archivo
├── LICENSE            # Licencia MIT
└── .gitignore         # Archivos ignorados por Git
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Ideas para Mejorar

- [ ] Añadir más operaciones lógicas (NAND, NOR)
- [ ] Implementar un algoritmo de entrenamiento automático
- [ ] Añadir visualización 3D para más entradas
- [ ] Implementar un perceptrón multicapa para resolver XOR
- [ ] Añadir exportación de parámetros entrenados

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Fernando Martin Montes Gonzalez** - [@ferdiex](https://github.com/ferdiex)

## 🙏 Agradecimientos

- Inspirado en los fundamentos de redes neuronales y el problema histórico del XOR
- Construido con [Streamlit](https://streamlit.io/) para crear interfaces interactivas fácilmente
- Visualizaciones con [Matplotlib](https://matplotlib.org/)

---

⭐ Si este proyecto te ayudó a entender los perceptrones, ¡dale una estrella!