# FreshCheckAI-RD15-SIC-ProyectoHackathon

**FreschCheckAI** es una aplicación web basada en Inteligencia Artificial diseñada para clasificar el estado de frescura de diversas frutas (manzanas, bananas y naranjas). Utilizando redes neuronales convolucionales (CNN), el sistema puede determinar si una fruta está **fresca**, **podrida** o **verde (inmadura)**.

## 🚀 Características

* **Detección en tiempo real:** Interfaz web intuitiva para subir imágenes y obtener resultados instantáneos.
* **Clasificación de 9 categorías:** Cubre manzanas, bananas y naranjas en tres estados diferentes.
* **Modelo de Deep Learning:** Entrenamiento basado en TensorFlow/Keras con una precisión superior al 98% en el set de entrenamiento.
* **Interfaz Moderna:** Diseño responsivo y limpio utilizando CSS personalizado y transiciones suaves.

## 🛠️ Tecnologías Utilizadas

* 
**Backend:** Python, Flask.


* **IA/ML:** TensorFlow, Keras, NumPy.
* **Procesamiento de Imágenes:** Pillow (PIL).
* **Frontend:** HTML5, CSS3 (Variables modernas, Flexbox), JavaScript (Fetch API).

## 📂 Estructura del Proyecto

```text
├── app.py              # Servidor Flask y API de predicción
├── IA.py               # Script de arquitectura y entrenamiento del modelo
├── Testing.py          # Script de prueba local para el modelo
├── verify_app.py       # Script de verificación de funcionamiento del servidor
[cite_start]├── requirements.txt    # Dependencias del proyecto [cite: 1]
├── clasificador_frutas.h5 # Modelo entrenado (generado tras IA.py)
├── static/
│   ├── style.css       # Estilos de la interfaz
│   └── script.js       # Lógica de carga y envío de imágenes
└── templates/
    └── index.html      # Página principal

```

## 📊 Capacidades de Clasificación

El modelo está entrenado para reconocer las siguientes clases:

1. Manzana fresca / podrida / verde
2. Banana fresca / podrida / verde
3. Naranja fresca / podrida / verde

## 🔧 Instalación y Uso

### 1. Clonar el repositorio y preparar el entorno

```bash
# Instalar las dependencias necesarias
pip install -r requirements.txt

```

### 2. Entrenamiento (Opcional)

Si deseas reentrenar el modelo con tus propios datos, coloca tu dataset en carpetas `train` y `test` dentro de una carpeta llamada `dataset` y ejecuta:

```bash
python IA.py

```

### 3. Ejecutar la Aplicación

Para iniciar el servidor web local:

```bash
python app.py

```

Luego, abre tu navegador en `http://127.0.0.1:5000`.

## 📈 Rendimiento del Modelo

Según los registros de entrenamiento, el modelo alcanza:

* **Precisión (Accuracy):** ~98.3% en la época 10.
* **Precisión de Validación:** ~89.2%.
* **Arquitectura:** 3 capas de Convolución (Conv2D) con MaxPooling seguidas de capas densas de clasificación.

---

**Desarrollado como una solución inteligente para la gestión de calidad de alimentos.**

---
