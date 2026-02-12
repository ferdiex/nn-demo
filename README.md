# 🧠 Demo Interactiva de Perceptrón

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-red)

## 📖 Descripción

Este es un proyecto educativo que presenta una **demo interactiva de perceptrones** para comprender los fundamentos de las redes neuronales. La aplicación permite visualizar y experimentar con perceptrones simples aplicados a operaciones lógicas básicas: **AND**, **OR** y **XOR**.

A través de una interfaz interactiva construida con Streamlit, los usuarios pueden ajustar los pesos y el bias del perceptrón en tiempo real y observar cómo estos cambios afectan la frontera de decisión y la capacidad del modelo para clasificar correctamente las entradas.

## ✨ Características Principales

- 🎮 **Interfaz interactiva** con controles deslizantes para ajustar parámetros en tiempo real
- 📊 **Visualización de la frontera de decisión** para cada configuración del perceptrón
- 📋 **Tabla de verdad comparativa** que muestra resultados esperados vs. obtenidos
- 🎯 **Tres operaciones lógicas**: AND, OR y XOR
- 📐 **Ecuación del perceptrón** mostrada dinámicamente
- 📚 **Contenido educativo** sobre el funcionamiento de perceptrones y sus limitaciones
- ✅ **Indicador de precisión** para evaluar el desempeño del modelo

## 🎬 Demostración

La aplicación permite experimentar con tres casos fundamentales:

### 1. Operación AND
El perceptrón aprende a devolver `1` solo cuando **ambas** entradas son `1`. Esta operación es **linealmente separable** y el perceptrón puede resolverla perfectamente con los pesos y bias correctos.

### 2. Operación OR
El perceptrón aprende a devolver `1` cuando **al menos una** entrada es `1`. También es **linealmente separable** y puede ser resuelta por un perceptrón simple.

### 3. Operación XOR
El perceptrón intenta aprender a devolver `1` cuando las entradas son **diferentes**. Esta operación **NO es linealmente separable**, demostrando una limitación fundamental de los perceptrones simples.

## 🔧 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Entorno virtual para aislar las dependencias

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ferdiex/nn-demo.git
cd nn-demo
```

### 2. Crear un entorno virtual (recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Uso

Para ejecutar la aplicación, simplemente ejecuta el siguiente comando en la terminal:

```bash
streamlit run nn_demo.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado (generalmente en `http://localhost:8501`).

### Cómo usar la aplicación:

1. **Selecciona una operación lógica** (AND, OR, o XOR) desde el menú lateral
2. **Ajusta los parámetros** usando los sliders:
   - `w1`: Peso de la primera entrada
   - `w2`: Peso de la segunda entrada
   - `b`: Bias (sesgo)
3. **Observa los cambios** en tiempo real:
   - La frontera de decisión en el gráfico
   - La tabla de verdad con resultados
   - La precisión del modelo

## 🧮 ¿Cómo Funciona un Perceptrón?

Un **perceptrón** es la unidad más básica de una red neuronal artificial, inventado por Frank Rosenblatt en 1957. Su funcionamiento se puede resumir en estos pasos:

### Proceso de Cálculo:

1. **Entradas**: El perceptrón recibe valores de entrada (x₁, x₂, ..., xₙ)
2. **Pesos**: Cada entrada se multiplica por su peso correspondiente (w₁, w₂, ..., wₙ)
3. **Suma ponderada**: Se calcula la suma de todas las entradas ponderadas más el bias:
   ```
   suma = w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ + b
   ```
4. **Función de activación**: Se aplica una función escalón:
   ```
   salida = 1 si suma ≥ 0
   salida = 0 si suma < 0
   ```

### Representación Geométrica:

La ecuación del perceptrón `w₁·x₁ + w₂·x₂ + b = 0` define una **línea recta** (en 2D) o un **hiperplano** (en dimensiones superiores) que divide el espacio en dos regiones. Los puntos de un lado se clasifican como `1` y los del otro como `0`.

## 📊 Los Tres Casos: AND, OR y XOR

### Tabla de Verdad

| x₁ | x₂ | AND | OR | XOR |
|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 1  |
| 1  | 0  | 0  | 1  | 1  |
| 1  | 1  | 1  | 1  | 0  |

### Configuraciones Óptimas:

**Para AND:**
- Pesos: w₁ = 1.0, w₂ = 1.0
- Bias: b = -1.5
- La frontera de decisión separa el punto (1,1) del resto

**Para OR:**
- Pesos: w₁ = 1.0, w₂ = 1.0
- Bias: b = -0.5
- La frontera de decisión separa (0,0) de los demás puntos

**Para XOR:**
- ⚠️ **No existe una configuración que funcione perfectamente**
- Ninguna línea recta puede separar correctamente los puntos

## ❌ ¿Por Qué XOR No es Linealmente Separable?

La operación XOR presenta un problema fundamental para los perceptrones simples:

- Los puntos (0,0) y (1,1) deben clasificarse como `0` (mismo color)
- Los puntos (0,1) y (1,0) deben clasificarse como `1` (mismo color)

**El problema:** No existe ninguna línea recta que pueda separar estos dos grupos. Los puntos están dispuestos de tal manera que cualquier línea que separe correctamente dos de ellos, incorrectamente clasificará los otros dos.

### Solución:

Para resolver XOR se necesita una **red neuronal multicapa** con al menos:
- Una capa de entrada (2 neuronas)
- Una capa oculta (2 neuronas mínimo)
- Una capa de salida (1 neurona)

Esto permite que la red cree una frontera de decisión no lineal que puede separar correctamente los puntos.

## 🎓 Conceptos Clave

- **Linealmente separable**: Un conjunto de datos es linealmente separable si existe un hiperplano que puede dividir perfectamente las clases.

- **Limitación del perceptrón**: Solo puede resolver problemas linealmente separables. Esta limitación llevó al desarrollo de redes neuronales multicapa.

- **Frontera de decisión**: La línea o superficie que separa las diferentes clases en el espacio de características.

- **Bias (sesgo)**: Permite desplazar la frontera de decisión, dándole al modelo más flexibilidad para ajustarse a los datos.

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para crear la interfaz web interactiva
- **NumPy**: Biblioteca para cálculos numéricos
- **Matplotlib**: Biblioteca para visualizaciones y gráficos

## 📂 Estructura del Proyecto

```
nn-demo/
│
├── nn_demo.py          # Aplicación principal de Streamlit
├── requirements.txt    # Dependencias del proyecto
├── .gitignore         # Archivos y carpetas ignorados por Git
├── LICENSE            # Licencia MIT
└── README.md          # Este archivo
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un Fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Fernando Martin Montes Gonzalez** (ferdiex)

## 🙏 Agradecimientos

Este proyecto fue creado con fines educativos para ayudar a comprender los fundamentos de las redes neuronales y las limitaciones de los perceptrones simples.

---

<div align="center">
  <p>Si este proyecto te fue útil, ¡no olvides darle una ⭐ en GitHub!</p>
  <p>Desarrollado con ❤️ para la comunidad de Machine Learning</p>
</div>
