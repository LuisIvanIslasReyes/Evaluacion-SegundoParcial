"""
Aplicación Flask para Predicción de Diabetes
Evaluación Segundo Parcial - Base de Datos

Esta aplicación web permite a los usuarios ingresar datos médicos
y obtener una predicción sobre el riesgo de diabetes utilizando
un modelo de Machine Learning previamente entrenado.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo y los objetos de preprocesamiento
MODEL_DIR = 'model_files'
model = joblib.load(os.path.join(MODEL_DIR, 'diabetes_model.joblib'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.joblib'))
model_info = joblib.load(os.path.join(MODEL_DIR, 'model_info.joblib'))

# Información sobre las características del modelo
FEATURE_NAMES = model_info['feature_names']
MODEL_NAME = model_info['model_name']
MODEL_ACCURACY = model_info['accuracy']

# Información sobre los rangos normales de cada característica
FEATURE_INFO = {
    'Pregnancies': {
        'label': 'Número de Embarazos',
        'description': 'Número de veces que ha estado embarazada',
        'min': 0,
        'max': 17,
        'step': 1,
        'unit': 'embarazos'
    },
    'Glucose': {
        'label': 'Nivel de Glucosa',
        'description': 'Concentración de glucosa en plasma a las 2 horas en una prueba oral de tolerancia a la glucosa',
        'min': 0,
        'max': 200,
        'step': 1,
        'unit': 'mg/dL'
    },
    'BloodPressure': {
        'label': 'Presión Arterial',
        'description': 'Presión arterial diastólica',
        'min': 0,
        'max': 122,
        'step': 1,
        'unit': 'mm Hg'
    },
    'SkinThickness': {
        'label': 'Grosor de Piel',
        'description': 'Grosor del pliegue cutáneo del tríceps',
        'min': 0,
        'max': 99,
        'step': 1,
        'unit': 'mm'
    },
    'Insulin': {
        'label': 'Insulina',
        'description': 'Insulina sérica a las 2 horas',
        'min': 0,
        'max': 846,
        'step': 1,
        'unit': 'μU/mL'
    },
    'BMI': {
        'label': 'Índice de Masa Corporal (IMC)',
        'description': 'Peso en kg / (altura en m)²',
        'min': 0,
        'max': 67.1,
        'step': 0.1,
        'unit': 'kg/m²'
    },
    'DiabetesPedigreeFunction': {
        'label': 'Función de Pedigree de Diabetes',
        'description': 'Función que representa la probabilidad de diabetes basada en el historial familiar',
        'min': 0.078,
        'max': 2.42,
        'step': 0.001,
        'unit': ''
    },
    'Age': {
        'label': 'Edad',
        'description': 'Edad del paciente en años',
        'min': 21,
        'max': 81,
        'step': 1,
        'unit': 'años'
    }
}


@app.route('/')
def index():
    """
    Página principal de la aplicación
    """
    return render_template('index.html', 
                         features=FEATURE_INFO,
                         model_name=MODEL_NAME,
                         accuracy=MODEL_ACCURACY)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para realizar predicciones
    Recibe los datos del formulario y devuelve la predicción
    """
    try:
        # Obtener los datos del formulario
        data = {}
        for feature in FEATURE_NAMES:
            value = request.form.get(feature)
            if value is None or value == '':
                return jsonify({
                    'error': f'Falta el valor para {feature}',
                    'success': False
                }), 400
            data[feature] = float(value)
        
        # Crear un DataFrame con los datos
        input_data = pd.DataFrame([data])
        
        # Escalar los datos
        input_scaled = scaler.transform(input_data)
        
        # Hacer la predicción
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        # Preparar la respuesta
        result = {
            'success': True,
            'prediction': int(prediction),
            'prediction_label': 'Diabetes' if prediction == 1 else 'No Diabetes',
            'probability_no_diabetes': float(probability[0] * 100),
            'probability_diabetes': float(probability[1] * 100),
            'input_data': data,
            'model_name': MODEL_NAME,
            'model_accuracy': float(MODEL_ACCURACY * 100)
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/about')
def about():
    """
    Página de información sobre el modelo
    """
    return render_template('about.html',
                         model_info=model_info,
                         feature_info=FEATURE_INFO)


if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug
    app.run(debug=True, host='0.0.0.0', port=5000)
