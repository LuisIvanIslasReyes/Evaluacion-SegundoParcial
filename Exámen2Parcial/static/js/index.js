const form = document.getElementById('predictionForm');
        const resultPlaceholder = document.getElementById('resultPlaceholder');
        const loadingIndicator = document.getElementById('loadingIndicator');
        const errorMessage = document.getElementById('errorMessage');
        const resultContent = document.getElementById('resultContent');
        const predictionCard = document.getElementById('predictionCard');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Hide previous results and show loading
            resultPlaceholder.style.display = 'none';
            resultContent.style.display = 'none';
            errorMessage.style.display = 'none';
            loadingIndicator.style.display = 'block';

            // Get form data
            const formData = new FormData(form);

            try {
                // Send request
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                // Hide loading
                loadingIndicator.style.display = 'none';

                if (data.success) {
                    // Show results
                    displayResults(data);
                } else {
                    // Show error
                    errorMessage.textContent = 'Error: ' + (data.error || 'Error desconocido');
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                // Hide loading and show error
                loadingIndicator.style.display = 'none';
                errorMessage.textContent = 'Error de conexión: ' + error.message;
                errorMessage.style.display = 'block';
            }
        });

        function displayResults(data) {
            // Update prediction card
            const isDiabetes = data.prediction === 1;
            
            if (isDiabetes) {
                predictionCard.classList.remove('no-diabetes');
                document.getElementById('predictionTitle').innerHTML = '<i class="fas fa-exclamation-triangle"></i>Resultado del Análisis';
                document.getElementById('predictionLabel').textContent = 'DIABETES';
                document.getElementById('predictionDescription').textContent = 
                    `Existe un ${data.probability_diabetes.toFixed(2)}% de probabilidad de diabetes`;
            } else {
                predictionCard.classList.add('no-diabetes');
                document.getElementById('predictionTitle').innerHTML = '<i class="fas fa-check-circle"></i>Resultado del Análisis';
                document.getElementById('predictionLabel').textContent = 'NO DIABETES';
                document.getElementById('predictionDescription').textContent = 
                    `Existe un ${data.probability_no_diabetes.toFixed(2)}% de probabilidad de NO tener diabetes`;
            }

            // Update probability bars
            const probNoDiabetes = data.probability_no_diabetes.toFixed(2);
            const probDiabetes = data.probability_diabetes.toFixed(2);

            document.getElementById('barNoDiabetes').style.width = probNoDiabetes + '%';
            document.getElementById('probNoDiabetes').textContent = probNoDiabetes + '%';

            document.getElementById('barDiabetes').style.width = probDiabetes + '%';
            document.getElementById('probDiabetes').textContent = probDiabetes + '%';

            // Update input summary
            const summaryGrid = document.getElementById('summaryGrid');
            summaryGrid.innerHTML = '';

            const featureLabels = {
                'Pregnancies': 'Embarazos',
                'Glucose': 'Glucosa',
                'BloodPressure': 'Presión Arterial',
                'SkinThickness': 'Grosor de Piel',
                'Insulin': 'Insulina',
                'BMI': 'IMC',
                'DiabetesPedigreeFunction': 'Pedigree',
                'Age': 'Edad'
            };

            for (const [key, value] of Object.entries(data.input_data)) {
                const summaryItem = document.createElement('div');
                summaryItem.className = 'summary-item';
                summaryItem.innerHTML = `
                    <strong>${featureLabels[key] || key}:</strong>
                    <span>${value}</span>
                `;
                summaryGrid.appendChild(summaryItem);
            }

            // Show results
            resultContent.style.display = 'block';
        }