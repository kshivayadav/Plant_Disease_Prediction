# AI Plant Health Advisor - Plant Disease Prediction

An AI-powered application to detect plant diseases from leaf images using Convolutional Neural Networks (CNN) and provide farmers with actionable insights using an open-source Large Language Model (Ollama). This tool helps farmers, gardeners, and researchers quickly identify plant diseases, understand their causes, and take preventive or remedial actions.

---

## Features

- **Plant Disease Detection:** Predicts multiple plant diseases from leaf images using a trained CNN model.
- **Actionable Recommendations:** Uses the open-source LLM (Ollama) to provide guidance, tips, and suggestions for managing plant health.
- **Image Upload Interface:** Easy-to-use web interface via Streamlit for uploading images.
- **Model Inference:** Fast and efficient inference using a saved model (`plant_disease_prediction_model.keras`).
- **Disease Details:** Provides descriptions, symptoms, and preventive measures for detected diseases.
- **Extensible:** Can be extended to add more crops, diseases, or enhanced LLM responses.

---

## Project Structure

Plant_Disease_prediction_CNN/
│

├── app.py # Streamlit app integrating CNN + LLM for disease detection and advice

├── main.py # Model training and inference scripts

├── trained_model/ # Folder containing saved CNN model

│ └── plant_disease_prediction_model.keras

├── class_indices.json # Mapping between class names and numerical labels

├── requirements.txt # Python dependencies
├── llm.py # Scripts interacting with the Ollama LLM for farmer suggestions

├── prompt.py # Prompts used for LLM to provide relevant advice

├── .gitignore

└── README.md

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **TensorFlow/Keras** (model training & inference)
- **NumPy** (numerical operations)
- **Pillow** (image preprocessing)
- **Streamlit** (web app interface)

---


## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/kshivayadav/Plant_Disease_Prediction.git
cd Plant_Disease_Prediction

python -m venv myenv
myenv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

streamlit run main.py

Open the link provided in your browser (usually http://localhost:8501).

Upload an image of a plant leaf to:

Get the predicted disease.

Receive detailed descriptions, preventive measures, and actionable advice from the integrated LLM.

## Model Details

Model type: Convolutional Neural Network (CNN)

Saved model: trained_model/plant_disease_prediction_model.keras

Class mapping: class_indices.json contains mapping of disease names to numerical labels.

LLM Integration: Uses Ollama open-source LLM to provide contextual guidance and recommendations for farmers.


## 📌 Future Improvements
- Add more plant species and disease classes
- Improve accuracy with transfer learning
- Deploy on cloud (Heroku, AWS, or Streamlit Cloud)

## 👨‍💻 Author
Developed by K Shiva Kumar ✨
Focused on building robust ML apps for real-world prediction tasks.


