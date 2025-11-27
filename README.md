# 🔭 Exoplanet Detection using Deep Learning (NASA Kepler Light Curves)

[![Streamlit App](https://img.shields.io/badge/🔭_Live_App-Streamlit-green?style=for-the-badge)](https://exoplanet-detection-using-deep-learning-hedt5bhak5gus223xxrcat.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/📂_Source_Code-GitHub-blue?style=for-the-badge)](https://github.com/ayushmandas29/Exoplanet-Detection-using-Deep-Learning)

---

## 🚀 Project Overview
This project uses **Deep Learning** to predict whether a star has an **orbiting exoplanet** by analysing its **light-curve signal captured by NASA's Kepler Space Telescope**.

When a planet passes in front of a star, the star’s brightness dips — this is known as a **transit**.  
Using this flux data, the trained 1D-CNN model classifies:

| Class | Meaning |
|-------|---------|
| 🌍 1 | **Exoplanet candidate detected** |
| ✖️ 0 | **No exoplanet detected** |

---

## 🌐 Live Interactive Web App
Upload a CSV file containing one row of flux values (light curve), and the model predicts instantly.

🔗 **Live Demo:**  
https://exoplanet-detection-using-deep-learning-hedt5bhak5gus223xxrcat.streamlit.app/

---

## 📂 Dataset
The model is trained using **NASA Kepler public light-curve dataset**, consisting of:
- **Exoplanet transit samples**
- **Non-transit samples**

Each sample contains ~3198 brightness readings over time.

---

## 🧠 Model Architecture
A custom **1D Convolutional Neural Network (CNN)**:
Input → Conv1D → MaxPool → Conv1D → MaxPool → Flatten → Dense → Dense (Sigmoid)


### 🏆 Achievements
| Metric | Value |
|--------|-------|
| Training Accuracy | ~99.6% |
| Validation Accuracy | ~99.5% |

---

## 🏛️ Project Files
| File | Description |
|------|-------------|
| `Exoplanet_Detection_using_Deep_Learning.ipynb` | Model training notebook |
| `best_model.keras` | Trained model |
| `exoplanet_app.py` | Streamlit web app |
| `requirements.txt` | Dependencies for deployment |
| `sample_lightcurve.csv` | Example input for prediction |

---

## 🚀 Run Locally (Optional)
```bash
pip install -r requirements.txt
streamlit run exoplanet_app.py

📌 How to Use the Web App
1. Export the light-curve flux values as a single-row CSV
2. Upload to the Streamlit interface

3. The model outputs:
     ✔ Prediction (Exoplanet / No Exoplanet)
     ✔ Probability score
     ✔ Light-curve visualization

| Feature                          | Status        |
| -------------------------------- | ------------- |
| Grad-CAM explanation heatmaps    | 🚧 (upcoming) |
| Predict transit depth & duration | 🚧            |
| Multi-file batch predictions     | 🚧            |
| FastAPI REST endpoint            | 🚧            |


👤 Author
Ayushman Das
Machine Learning & AI Enthusiast
📧 ayushmandas736@gmail.com
🔗 https://github.com/ayushmandas29

⭐ If you like this project, consider giving it a star — it motivates further research and improvements!
