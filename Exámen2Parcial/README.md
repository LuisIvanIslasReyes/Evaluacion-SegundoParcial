#  Sistema de Predicción de Diabetes

## Evaluación Segundo Parcial - Base de Datos

Este proyecto implementa un sistema completo de predicción de diabetes utilizando Machine Learning y una interfaz web interactiva.

---

## Descripción del Proyecto

### Parte 1: Análisis y Entrenamiento del Modelo
- ✅ Análisis Exploratorio de Datos (EDA)
- ✅ Preprocesamiento y limpieza de datos
- ✅ Entrenamiento de múltiples modelos (Logistic Regression, KNN, Random Forest)
- ✅ Optimización con GridSearchCV
- ✅ Evaluación exhaustiva con múltiples métricas

### Parte 2: Despliegue Web
- ✅ Persistencia del modelo con joblib
- ✅ Aplicación web con Flask
- ✅ Interfaz de usuario intuitiva
- ✅ Sistema de predicción en tiempo real

---

## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd Exámen2Parcial
   ```

2. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generar los archivos del modelo**
   - Abrir el notebook `Examen_Diabetes_Prediction.ipynb`
   - Ejecutar todas las celdas hasta la Parte 2
   - Esto generará la carpeta `model_files` con:
     - `diabetes_model.joblib`
     - `scaler.joblib`
     - `model_info.joblib`

4. **Ejecutar la aplicación web**
   ```bash
   python app.py
   ```

5. **Abrir el navegador**
   - Ir a: `http://localhost:5000`

---

## Estructura del Proyecto

```
Exámen2Parcial/
│
├── app.py                              # Aplicación Flask principal
├── requirements.txt                     # Dependencias del proyecto
├── README.md                           # Este archivo
│
├── Examen_Diabetes_Prediction.ipynb    # Notebook con análisis y modelo
├── diabetes.csv                        # Dataset de diabetes
│
├── model_files/                        # Archivos del modelo (generados)
│   ├── diabetes_model.joblib           # Modelo entrenado
│   ├── scaler.joblib                   # Objeto StandardScaler
│   └── model_info.joblib               # Información del modelo
│
└── templates/                          # Plantillas HTML
    ├── index.html                      # Página principal
    └── about.html                      # Página de información
```

---

## Uso de la Aplicación

### Página Principal
1. **Ingresar los datos del paciente** en el formulario:
   - Número de embarazos
   - Nivel de glucosa
   - Presión arterial
   - Grosor de piel
   - Insulina
   - IMC (Índice de Masa Corporal)
   - Función de pedigree de diabetes
   - Edad

2. **Hacer clic en "Realizar Predicción"**

3. **Ver los resultados**:
   - Predicción (Diabetes o No Diabetes)
   - Probabilidades porcentuales
   - Resumen de datos ingresados

### Página "Acerca del Modelo"
- Información técnica del modelo
- Métricas de rendimiento
- Características utilizadas
- Tecnologías empleadas

---

##  Información del Modelo

### Modelo Seleccionado
**Random Forest (Original)**
- Accuracy: 77.92%
- Precision: 0.7174
- Recall: 0.6111
- F1-Score: 0.6600
- AUC: 0.8179

### Características Utilizadas (8 features)
1. **Pregnancies** - Número de embarazos
2. **Glucose** - Nivel de glucosa en plasma
3. **BloodPressure** - Presión arterial diastólica
4. **SkinThickness** - Grosor del pliegue cutáneo
5. **Insulin** - Insulina sérica
6. **BMI** - Índice de masa corporal
7. **DiabetesPedigreeFunction** - Probabilidad basada en historial familiar
8. **Age** - Edad del paciente

---

##  Tecnologías Utilizadas

### Backend
- **Python 3.x**
- **Flask** - Framework web
- **scikit-learn** - Machine Learning
- **pandas** - Manipulación de datos
- **NumPy** - Computación numérica
- **joblib** - Persistencia de modelos

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript (Vanilla)**

---

## Endpoints de la API

### GET /
Página principal con el formulario de predicción

### POST /predict
Realiza una predicción
- **Input**: FormData con las 8 características
- **Output**: JSON con predicción y probabilidades

### GET /about
Página con información del modelo

---

## Ejemplos de Uso

### Ejemplo 1: Paciente con alto riesgo
```
Embarazos: 6
Glucosa: 148
Presión Arterial: 72
Grosor de Piel: 35
Insulina: 125
IMC: 33.6
Pedigree: 0.627
Edad: 50

Resultado: DIABETES (71.94% probabilidad)
```

### Ejemplo 2: Paciente con bajo riesgo
```
Embarazos: 1
Glucosa: 85
Presión Arterial: 66
Grosor de Piel: 29
Insulina: 85
IMC: 26.6
Pedigree: 0.351
Edad: 31

Resultado: NO DIABETES (97.42% probabilidad)
```

---

##  Importante

Este sistema es un **proyecto académico y educativo**. No debe utilizarse como sustituto del diagnóstico médico profesional. Siempre consulte a un profesional de la salud para obtener un diagnóstico y tratamiento adecuado.

---

##  Desarrollo

**Proyecto desarrollado para:**
- Materia: Base de Datos
- Evaluación: Segundo Parcial
- Universidad Tecnológica de Tijuana

---

##  Notas Adicionales

- La aplicación corre por defecto en `http://localhost:5000`
- El modo debug está activado para desarrollo
- Los archivos del modelo deben existir en la carpeta `model_files`
- Se requiere ejecutar el notebook completo antes de usar la aplicación web

---

## Solución de Problemas

### Error: "No such file or directory: 'model_files/...'"
**Solución:** Ejecutar el notebook `Examen_Diabetes_Prediction.ipynb` hasta la sección de Parte 2 para generar los archivos del modelo.

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solución:** Instalar las dependencias con `pip install -r requirements.txt`

### La aplicación no carga en el navegador
**Solución:** Verificar que el puerto 5000 no esté siendo usado por otra aplicación.

---

##  Licencia

Examen académico - Universidad Tecnológica de Tijuana

---

**¡Gracias por revisar este proyecto!** 🎓
